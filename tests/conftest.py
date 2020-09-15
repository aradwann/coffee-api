import pytest
from app import create_app
from mongoengine import connect, disconnect


@pytest.fixture()
def client():
    flask_app = create_app('testing')

    # Flask provides a way to test your app
    # by exposing the Werkzeug test Client
    # and handling the context locals for you.
    client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
    # connect to a mongo mock db for testing
    connect('mongoenginetest', host='mongomock://localhost', alias='testdb')

    yield client  # this is where the testing happens!

    # tear down the connection to mongo mock
    disconnect()
    ctx.pop()
