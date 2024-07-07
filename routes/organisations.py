from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from models import Organisation, User
from schemas import user_schema, organisation_schema
from flask import Blueprint
import uuid

organisations_bp = Blueprint('organisations', __name__)

@organisations_bp.route('', methods=['GET'])
@jwt_required()
def get_user_organisations():
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(userId=current_user_id).first()
    if user:
        organisations = user.organisations
        orgs = [{"orgId": org.orgId, "name": org.name, "description": org.description} for org in organisations]
        return jsonify({
            "status": "success",
            "message": "Organisations retrieved",
            "data": {"organisations": orgs}
        }), 200
    else:
        return jsonify({"status": "Bad request", "message": "User not found", "statusCode": 404}), 404

@organisations_bp.route('<string:org_id>', methods=['GET'])
@jwt_required()
def get_organisation(org_id):
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(userId=current_user_id).first()
    org = Organisation.query.filter_by(orgId=org_id).first()
    if (org and user) and (user in org.users):
        return jsonify({
            "status": "success",
            "message": "Organisation retrieved",
            "data": {
                "orgId": org.orgId,
                "name": org.name,
                "description": org.description
            }
        }), 200
    else:
        return jsonify({"status": "Bad request", "message": "Organisation not found", "statusCode": 404}), 404

@organisations_bp.route('', methods=['POST'])
@jwt_required()
def create_organisation():
    data = request.get_json()

    current_user_id = get_jwt_identity()
    user = User.query.filter_by(userId=current_user_id).first()
    if user:
        orgId = str(uuid.uuid4())
        new_org = Organisation(
            orgId=orgId,
            name=data['name'],
            description=data.get('description', '')
        )
        new_org.users.append(user)
        db.session.add(new_org)
        db.session.commit()
        return jsonify({
            "status": "success",
            "message": "Organisation created successfully",
            "data": {
                "orgId": new_org.orgId,
                "name": new_org.name,
                "description": new_org.description
            }
        }), 201
    else:
        return jsonify({
            "status": "Bad request",
            "message": "Client error",
            "statusCode": 400}), 400

@organisations_bp.route('<string:org_id>/users', methods=['POST'])
@jwt_required()
def add_user_to_organisation(org_id):
    data = request.get_json()
    if not data or not data.get('userId'):
        return jsonify({"status": "Bad request", "message": "Invalid data", "statusCode": 400}), 400

    current_user_id = get_jwt_identity()
    org = Organisation.query.filter_by(orgId=org_id).first()
    user = User.query.filter_by(userId=data['userId']).first()
    if org and user:
        org.users.append(user)
        db.session.commit()
        return jsonify({
            "status": "success",
            "message": "User added to organisation successfully"
            }), 200
    else:
        return jsonify({
            "status": "Bad request",
            "message": "User or organisation not found",
            "statusCode": 404
            }), 404
