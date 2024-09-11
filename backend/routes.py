from flask import Blueprint, jsonify, request
from models import db, User, Children, Caregiver, Finance, Attendance, Enrollment
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_swagger_ui import get_swaggerui_blueprint

api_bp = Blueprint('api', __name__)

# SWAGGER setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)

# User Registration
@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify(message="Missing required fields"), 400

    if User.query.filter_by(username=username).first():
        return jsonify(message="User already exists"), 400

    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User registered successfully"), 201

# User Login
@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(message="Missing username or password"), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

# Get Children List (with pagination)
@api_bp.route('/children', methods=['GET'])
@jwt_required()
def get_children():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    children = Children.query.paginate(page, per_page, error_out=False)

    if not children.items:
        return jsonify(message="No children found"), 404

    return jsonify({
        'children': [child.serialize() for child in children.items],
        'total': children.total,
        'pages': children.pages,
        'page': children.page
    }), 200

# Get Caregivers
@api_bp.route('/caregivers', methods=['GET'])
@jwt_required()
def get_caregivers():
    caregivers = Caregiver.query.all()

    if not caregivers:
        return jsonify(message="No caregivers found"), 404

    return jsonify([caregiver.serialize() for caregiver in caregivers]), 200

# Add a Child
@api_bp.route('/children', methods=['POST'])
@jwt_required()
def add_child():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    caregiver_id = data.get('caregiver_id')

    if not name or not age or not caregiver_id:
        return jsonify(message="Missing required fields"), 400

    if not Caregiver.query.get(caregiver_id):
        return jsonify(message="Caregiver not found"), 404

    new_child = Children(name=name, age=age, caregiver_id=caregiver_id)
    db.session.add(new_child)
    db.session.commit()

    return jsonify(message="Child added successfully"), 201

# Get Child by ID
@api_bp.route('/children/<int:child_id>', methods=['GET'])
@jwt_required()
def get_child(child_id):
    child = Children.query.get_or_404(child_id)
    return jsonify(child.serialize()), 200

# Update Child by ID
@api_bp.route('/children/<int:child_id>', methods=['PUT'])
@jwt_required()
def update_child(child_id):
    data = request.get_json()
    child = Children.query.get_or_404(child_id)

    child.name = data.get('name', child.name)
    child.age = data.get('age', child.age)
    caregiver_id = data.get('caregiver_id')

    if caregiver_id:
        caregiver = Caregiver.query.get(caregiver_id)
        if caregiver:
            child.caregiver_id = caregiver_id
        else:
            return jsonify(message="Caregiver not found"), 404

    db.session.commit()
    return jsonify(message="Child updated successfully"), 200

# Delete Child by ID
@api_bp.route('/children/<int:child_id>', methods=['DELETE'])
@jwt_required()
def delete_child(child_id):
    child = Children.query.get_or_404(child_id)
    db.session.delete(child)
    db.session.commit()

    return jsonify(message="Child deleted successfully"), 200

# Financial Data (CRUD)
@api_bp.route('/finances', methods=['POST'])
@jwt_required()
def add_finance():
    data = request.get_json()
    amount = data.get('amount')
    description = data.get('description')

    if not amount or not description:
        return jsonify(message="Missing required fields"), 400

    finance = Finance(amount=amount, description=description)
    db.session.add(finance)
    db.session.commit()

    return jsonify(message="Finance record added successfully"), 201

@api_bp.route('/finances', methods=['GET'])
@jwt_required()
def get_finances():
    finances = Finance.query.all()
    return jsonify([finance.serialize() for finance in finances]), 200

# Attendance Data (CRUD)
@api_bp.route('/attendance', methods=['POST'])
@jwt_required()
def add_attendance():
    data = request.get_json()
    date = data.get('date')
    status = data.get('status')

    if not date or not status:
        return jsonify(message="Missing required fields"), 400

    attendance = Attendance(date=date, status=status)
    db.session.add(attendance)
    db.session.commit()

    return jsonify(message="Attendance record added successfully"), 201

@api_bp.route('/attendance', methods=['GET'])
@jwt_required()
def get_attendance():
    attendance_records = Attendance.query.all()
    return jsonify([attendance.serialize() for attendance in attendance_records]), 200

# Enrollment Data (CRUD)
@api_bp.route('/enrollments', methods=['POST'])
@jwt_required()
def add_enrollment():
    data = request.get_json()
    child_id = data.get('child_id')
    enrollment_date = data.get('enrollment_date')

    if not child_id or not enrollment_date:
        return jsonify(message="Missing required fields"), 400

    enrollment = Enrollment(child_id=child_id, enrollment_date=enrollment_date)
    db.session.add(enrollment)
    db.session.commit()

    return jsonify(message="Enrollment record added successfully"), 201

@api_bp.route('/enrollments', methods=['GET'])
@jwt_required()
def get_enrollments():
    enrollments = Enrollment.query.all()
    return jsonify([enrollment.serialize() for enrollment in enrollments]), 200

# Error Handling for non-existent resources
@api_bp.errorhandler(404)
def resource_not_found(error):
    return jsonify(message="Resource not found"), 404

@api_bp.errorhandler(500)
def internal_server_error(error):
    return jsonify(message="Internal server error"), 500

# Swagger Endpoint
@api_bp.route('/swagger', methods=['GET'])
def swagger_docs():
    return jsonify(message="Swagger API documentation available at /swagger")
