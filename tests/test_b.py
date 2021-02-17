from . import client
import json


# Testing if a user with valid credentials
# can login successfully
def test_user_login_pass():
    response = client.post(
        "/user/login",
        json={
            "username": "Antony",
            "password": "string",
        }
    )

    assert response.status_code == 200
    # TODO: test json response returned


# Testing if a user with invalid credentials
# fails to login successfully
def test_user_login_fail():

    # invalid user name
    response = client.post(
        "/user/login",
        json={
            "username": "test",
            "password": "string",
        }
    )

    assert response.status_code == 200
    assert response.json() == {'status':'failed','message':'Invalid Login'}

    # Invalid password
    response = client.post(
        "/user/login",
        json={
            "username": "Peter",
            "password": "pass",
        }
    )

    assert response.status_code == 200
    assert response.json() == {'status':'failed','message':'Invalid Login'}