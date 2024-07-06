import unittest
from flask_testing import TestCase
from app import create_app
from extensions import db
from config import TestConfig
from models import User
from flask_jwt_extended import create_access_token, decode_token
import time
import datetime
app = create_app(TestConfig)

class TokenTests(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

    def create_app(self):
        app = create_app(TestConfig)
        app.config.from_object(self)
        return app

    def setUp(self):
        db.create_all()
        self.user = User(
            userId="unique_user_id",
            firstName="John",
            lastName="Doe",
            email="john.doe@example.com",
            password="hashed_password",
            phone="1234567890"
        )
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_token_generation(self):
        access_token = create_access_token(identity=self.user.userId)
        decoded_token = decode_token(access_token)
        self.assertEqual(decoded_token['sub'], self.user.userId)

    def test_token_expiration(self):
        app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 1  # 1 second for testing
        access_token = create_access_token(
            identity=self.user.userId,
            expires_delta=datetime.timedelta(seconds=2)
            )
        time.sleep(4)  # Sleep for 4 seconds to ensure token expiration
        with self.assertRaises(Exception):
            decode_token(access_token)

if __name__ == '__main__':
    unittest.main()
