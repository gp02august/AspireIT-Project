from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate
from flask_swagger_ui import get_swaggerui_blueprint
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)  # Fixed to __name_

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY')

# Explicitly set development environment and debug mode
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager(app)

# Properly set up CORS for all API routes (allow all origins for dev)
CORS(app, resources={r"/": {"origins": ""}})  # Use "*" to allow all origins during development

migrate = Migrate(app, db)

# Properly initialize SQLAlchemy with the app
db.init_app(app)

# Create tables automatically after app starts (within app context)
with app.app_context():
    db.create_all()

# Setup Swagger UI
SWAGGER_URL = '/swagger'  # URL for accessing the Swagger UI
API_URL = '/swagger.json'  # Path to Swagger JSON file
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Swagger UI configuration options
        'app_name': "Flask API Documentation"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return "Flask is running!"

# Swagger JSON file route
@app.route('/swagger.json')
def swagger_json():
    return send_from_directory('.', 'swagger.json')

# Error handling route for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Add error handling route for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Resource not found"}), 404

# Main entry point
if __name__ == "__main__":  # Fixed to __name_ and _main_
    # Import the API routes blueprint from routes.py
    from routes import api_bp
    # Register the blueprint with a prefix for all API routes
    app.register_blueprint(api_bp, url_prefix='/api')

    # Start the Flask application
    app.run(debug=True)