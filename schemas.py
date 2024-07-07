from app import ma
from marshmallow import Schema, fields, validate, ValidationError

class UserSchema(ma.Schema):
    userId = fields.String(validate=validate.Length(min=1))
    firstName = fields.String(required=True, validate=validate.Length(min=1))
    lastName = fields.String(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=validate.Length(min=6))
    phone = fields.String(validate=validate.Length(min=10, max=15))

class OrganisationSchema(ma.Schema):
    orgId = fields.String(validate=validate.Length(min=1))
    name = fields.String(required=True, validate=validate.Length(min=1))
    description = fields.String()

user_schema = UserSchema()
organisation_schema = OrganisationSchema()
