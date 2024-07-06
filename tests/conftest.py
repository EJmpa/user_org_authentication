import pytest
from app import create_app
from extensions import db 
from config import TestConfig

@pytest.fixture(scope='session')
def app():
    app = create_app(TestConfig)
    with app.app_context():
        yield app

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        db.create_all()
        yield db.session
        db.session.remove()
        db.drop_all()




# @pytest.fixture(scope='session')
# def app():
#     app = create_app(TestConfig)
#     with app.app_context():
#         yield app

# @pytest.fixture(scope='session')
# def db(app):
#     _db.app = app
#     _db.create_all()
#     yield _db
#     _db.drop_all()

# @pytest.fixture(scope='function')
# def session(db):
#     connection = db.engine.connect()
#     transaction = connection.begin()

#     options = dict(bind=connection, binds={})
#     session = db.create_scoped_session(options=options)

#     db.session = session

#     yield session

#     transaction.rollback()
#     connection.close()
#     session.remove()

# @pytest.fixture(scope='function')
# def client(app):
#     return app.test_client()
