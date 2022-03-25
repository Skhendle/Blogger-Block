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

    assert response.status_code == 201
    assert response.json() == {
        "message": "Successful Login",
        "user_data": {
            "id": 3,
            "username": "Antony",
            "age": 25,
            "gender": "male"
        }
    }


# Testing if a user with invalid credentials
# fails to login successfully
def test_invalid_user_name():
    # invalid user name
    response = client.post(
        "/user/login",
        json={
            "username": "test",
            "password": "string",
        }
    )
    assert response.status_code == 400
    assert response.json()['detail'] == 'Invalid Login'


def test_invalid_user_name():
    # Invalid password
    response = client.post(
        "/user/login",
        json={
            "username": "Peter",
            "password": "pass",
        }
    )

    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid Login'