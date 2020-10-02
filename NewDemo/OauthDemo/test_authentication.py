import pytest

from OauthDemo import app, registration, objects
from wtforms import Form

def test_register(client, app):
    # Assert registration page is accessible
    assert client.get("/register").status_code == 200

    # Test successful registration redirects to "registration successful" page
    registrationForm = RegistrationForm()
    registrationForm.fname.value = "TEST"
    registrationForm.lname.value = "USER"
    registrationForm.password.value = "password123"
    response =  client.post("/register", data=registrationForm.data, follow_redirects=True).status_code

    assert response.status_code == 200
    assert response.headers["Location"] == "http://localhost:5000/login"