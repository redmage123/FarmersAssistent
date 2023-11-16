from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# Initialize SQLAlchemy ORM
db = SQLAlchemy()

def create_app():
    # Initialize Flask app
    app = Flask(__name__)
    Bootstrap(app)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farmers_assistant.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize SQLAlchemy with app context
    db.init_app(app)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Import and register Blueprints here
    # Assuming you have a views blueprint in your templates directory
    from .templates import views as views_blueprint
    app.register_blueprint(views_blueprint)

    # Setup login manager user loader
    from .models.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Create all database tables
    with app.app_context():
        db.create_all()

    return app
