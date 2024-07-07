from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import User
from flask import Blueprint

users_bp = Blueprint('users', __name__)

@users_bp.route('<string:user_id>', methods=['GET'])
@jwt_required()
def get_user(id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(userId=id).first()
    if user and user.userId == current_user_id:
        return jsonify({
            "status": "success",
            "message": "User retrieved",
            "data": {
                "userId": user.userId,
                "firstName": user.firstName,
                "lastName": user.lastName,
                "email": user.email,
                "phone": user.phone
            }
        }), 200
    else:
        return jsonify({
            "status": "Bad request",
            "message": "User not found",
            "statusCode": 404
            }), 404
