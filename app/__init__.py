from flask import Flask
from app.models.model import db
from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.employee import employee_bp
from app.routes.report import report_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'dev_secret_key_change_in_production'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:database@localhost/test_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(report_bp)

    # Create Database Tables
    with app.app_context():
        db.create_all()

    return app
