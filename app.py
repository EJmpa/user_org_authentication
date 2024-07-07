from flask import Flask
from config import Config
from extensions import db, ma, jwt
from flask_migrate import Migrate
from utils.helpers import bcrypt


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    migrate = Migrate(app, db)

    with app.app_context():
        from routes.auth import auth_bp
        from routes.users import users_bp
        from routes.organisations import organisations_bp
        
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(users_bp, url_prefix='/api/users')
        app.register_blueprint(organisations_bp, url_prefix='/api/organisations')
        
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
