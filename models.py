from extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    userId = db.Column(db.String, unique=True, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=True)

class Organisation(db.Model):
    __tablename__ = 'organisations'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    orgId = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    users = db.relationship('User', secondary='user_organisation', backref='organisations')

user_organisation = db.Table('user_organisation',
    db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('users.id')),
    db.Column('organisation_id', UUID(as_uuid=True), db.ForeignKey('organisations.id'))
)
