from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from routes import register_blueprints


app = Flask(__name__)


db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

register_blueprints(app)

if __name__ == "__main__":
    app.run()

# def create_app():
#     app = Flask(__name__)
#     app.config.from_object(Config)

#     db.init_app(app)
#     ma.init_app(app)
#     jwt = JWTManager(app)

#     register_blueprints(app)

#     return app

# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True)
