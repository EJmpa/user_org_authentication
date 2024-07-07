from flask import request, jsonify
from flask_jwt_extended import create_access_token
from extensions import db
from flask import Blueprint
from models import User, Organisation
from schemas import user_schema, organisation_schema
from utils.helpers import hash_password, check_password
from marshmallow import ValidationError
import uuid
import datetime

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    try:
        user_data = user_schema.load(data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 422
    
    
    existing_user = User.query.filter_by(email=user_data['email']).first()
    if existing_user:
        return jsonify({"errors": [{"field": "email", "message": "Email already registered"}]}), 422

    try:
        hashed_password = hash_password(data['password'])

        new_user = User(
            userId=str(uuid.uuid4()),
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            password=hashed_password,
            phone=data['phone']
        )

        db.session.add(new_user)
        db.session.commit()

        orgId = str(uuid.uuid4())
        org_name = f"{new_user.firstName}'s Organisation"
        new_org = Organisation(
            orgId=orgId,
            name=org_name,
            description=f"Organisation for {new_user.firstName}"
        )

        new_org.users.append(new_user)
        db.session.add(new_org)
        db.session.commit()

        access_token = create_access_token(
            identity=new_user.userId, expires_delta=datetime.timedelta(hours=1)
            )
        return jsonify({
            "status": "success",
            "message": "Registration successful",
            "data": {
                "accessToken": access_token,
                "user": {
                    "userId": new_user.userId,
                    "firstName": new_user.firstName,
                    "lastName": new_user.lastName,
                    "email": new_user.email,
                    "phone": new_user.phone,
                }
            }
        }), 201

    except Exception as e:
        return jsonify({
            "status": "Bad request",
            "message": "Registration unsuccessful",
            "statusCode": 400
            }), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data['email']).first()
   
   
    
    if user and check_password(user.password, data['password']):
        access_token = create_access_token(
            identity=user.userId,
            expires_delta=datetime.timedelta(hours=1)
            )
        return jsonify({
            "status": "success",
            "message": "Login successful",
            "data": {
                "accessToken": access_token,
                "user": {
                    "userId": user.userId,
                    "firstName": user.firstName,
                    "lastName": user.lastName,
                    "email": user.email,
                    "phone": user.phone,
                }
            }
        }), 200
    else:
        return jsonify({
            "status": "Bad request",
            "message": "Authentication failed",
            "statusCode": 401
            }), 401
