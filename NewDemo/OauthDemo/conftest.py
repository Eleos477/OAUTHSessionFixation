# Basic Structure Derived from https://flask.palletsprojects.com/en/1.1.x/testing/#the-testing-skeleton

import os
import tempfile

import pytest

import app
import model

@pytest.fixture
def app():
    """Creates the test app instance"""
    # Get temporary file for file storage
    usersFilename, usersFilepath = tempfile.mkstemp()
    testConfig = {
        "TWITTER_CLIENT_ID": '4kQ2lYO4QbTPYzlktumoypPZX',
        "TWITTER_CLIENT_SECRET": 'Of6038YMKPgVvKFjaMfU5lJa9ASK9kLTK7VjNlOOxF8iSOn0Z3',
        "REGISTERED_USERS_SAVE": usersFilepath
    }

    # Initialise the app and reset the model
    model.reinitialise()
    testApp = app.initialiseApp()
    
    yield testApp

    os.close(usersFilename)
    os.unlink

    return testApp

@pytest.fixture
def client(app):
    
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()