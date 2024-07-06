import unittest
from flask_testing import TestCase
from app import create_app
from extensions import db
from models import User, Organisation
from flask_jwt_extended import create_access_token
from config import TestConfig

class OrganisationTests(TestCase):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True

    def create_app(self):
        app = create_app(TestConfig)
        app.config.from_object(self)
        return app

    def setUp(self):
        db.create_all()
        self.user1 = User(
            userId="user1",
            firstName="John",
            lastName="Doe",
            email="john.doe@example.com",
            password="hashed_password",
            phone="1234567890"
        )
        self.user2 = User(
            userId="user2",
            firstName="Jane",
            lastName="Doe",
            email="jane.doe@example.com",
            password="hashed_password",
            phone="0987654321"
        )
        db.session.add(self.user1)
        db.session.add(self.user2)
        db.session.commit()

        self.org1 = Organisation(
            orgId="org1",
            name="John's Organisation",
            description="Organisation for John"
        )
        self.org1.users.append(self.user1)
        db.session.add(self.org1)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_user_access_own_organisation(self):
        access_token = create_access_token(identity=self.user1.userId)
        response = self.client.get('/api/organisations/org1', headers={
            'Authorization': f'Bearer {access_token}'
        })
        self.assertEqual(response.status_code, 200)
        data = response.json['data']
        self.assertEqual(data['orgId'], 'org1')
        self.assertEqual(data['name'], "John's Organisation")

    def test_user_cannot_access_other_organisation(self):
        access_token = create_access_token(identity=self.user2.userId)
        response = self.client.get('/api/organisations/org1', headers={
            'Authorization': f'Bearer {access_token}'
        })
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
