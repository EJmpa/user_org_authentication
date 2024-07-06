from flask import Blueprint
from .auth import auth_bp
from .users import users_bp
from .organisations import organisations_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(organisations_bp, url_prefix='/api/organisations')

# Define the blueprint for routes module itself if needed
routes_bp = Blueprint('routes', __name__)
