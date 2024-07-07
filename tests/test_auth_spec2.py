import unittest
from flask_testing import TestCase
from extensions import db
from app import create_app
from models import User, Organisation
from flask_jwt_extended import decode_token
from config import TestConfig

app = create_app(TestConfig)

class AuthTests(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

    def create_app(self):
        app = create_app(TestConfig)
        app.config.from_object(self)
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user_successfully(self):
        response = self.client.post('/auth/register', json={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890"
        })
        print('Register Response:', response.json)  # Debugging print
        self.assertEqual(response.status_code, 201)
        data = response.json['data']
        self.assertIn('accessToken', data)
        self.assertEqual(data['user']['firstName'], 'John')
        self.assertEqual(data['user']['lastName'], 'Doe')
        self.assertEqual(data['user']['email'], 'john.doe@example.com')
        self.assertEqual(data['user']['phone'], '1234567890')
        org = Organisation.query.first()
        self.assertEqual(org.name, "John's Organisation")

    def test_login_user_successfully(self):
        self.client.post('/auth/register', json={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890"
        })
        response = self.client.post('/auth/login', json={
            "email": "john.doe@example.com",
            "password": "password123"
        })
        print('Login Response:', response.json)  # Debugging print
        self.assertEqual(response.status_code, 200)
        data = response.json['data']
        self.assertIn('accessToken', data)
        self.assertEqual(data['user']['firstName'], 'John')

    def test_register_missing_fields(self):
        response = self.client.post('/auth/register', json={
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', response.json)

        response = self.client.post('/auth/register', json={
            "firstName": "John",
            "email": "john.doe@example.com",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', response.json)

        response = self.client.post('/auth/register', json={
            "firstName": "John",
            "lastName": "Doe",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', response.json)

        response = self.client.post('/auth/register', json={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com"
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', response.json)

    def test_register_duplicate_email(self):
        self.client.post('/auth/register', json={
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "1234567890"
        })
        response = self.client.post('/auth/register', json={
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "password": "password123",
            "phone": "0987654321"
        })
        self.assertEqual(response.status_code, 422)
        self.assertIn('errors', response.json)

if __name__ == '__main__':
    unittest.main()
