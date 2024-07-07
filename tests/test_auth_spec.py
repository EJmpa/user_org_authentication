import datetime
import pytest
from flask_jwt_extended import create_access_token, JWTManager, decode_token
from app import create_app

app = create_app()

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['JWT_SECRET_KEY'] = 'test_secret'
    JWTManager(app)
    with app.app_context():
        yield app.test_client()

def test_token_generation(client):
    with app.app_context():
        user_id = 'user123'
        user_data = {
            'userId': user_id,      
            'firstName': 'John',    
            'lastName': 'Doe',      
            'email': 'john.doe@example.com',
            'phone': '1234567890'   
        }

        # Generate access token with additional claims
        access_token = create_access_token(identity=user_id, additional_claims=user_data, expires_delta=datetime.timedelta(seconds=30))

        # Decode token to verify user data
        decoded_token = decode_token(access_token)

        assert decoded_token['sub'] == user_id 
        # Adjusted assertion to check for additional claims directly
        for key, value in user_data.items():
            assert decoded_token[key] == value