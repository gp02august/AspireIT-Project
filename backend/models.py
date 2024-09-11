from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

# User model for authentication
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    # Hash the password and store it securely
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check if the provided password matches the hashed password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Children model for storing children data
class Children(db.Model):
    __tablename__ = 'children'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # Serialize the data for JSON response
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }

# Caregiver model for storing caregiver data
class Caregiver(db.Model):
    __tablename__ = 'caregivers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Finance model for storing financial transactions
class Finance(db.Model):
    __tablename__ = 'finances'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Attendance model for tracking attendance records
class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(10), nullable=False)

    # Relationship with the child model
    child = db.relationship('Children', backref=db.backref('attendance_records', lazy=True))

# Enrollment model for storing children's enrollment details
class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.id'), nullable=False)
    date_enrolled = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with the child model
    child = db.relationship('Children', backref=db.backref('enrollments', lazy=True))


    