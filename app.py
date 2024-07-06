from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    ma.init_app(app)
    JWTManager(app)

    with app.app_context():
        from .routes.auth import auth_bp
        from .routes.users import users_bp
        from .routes.organisations import organisations_bp
        
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(users_bp, url_prefix='/api/users')
        app.register_blueprint(organisations_bp, url_prefix='/api/organisations')
        
        db.create_all()

    return app
