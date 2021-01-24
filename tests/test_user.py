from . import client
import json

#testing the main page
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Welcome To"}


# Tesing the login function
# valid inputs
def test_user_login_pass():
    response = client.post(
        "/user/login",
        json={
            "username": "Peter",
            "password": "string",
        }
    )


    assert response.status_code == 200


# Tesing the login function
# invalid inputs: username
def test_user_login_fail0():
    response = client.post(
        "/user/login",
        json={
            "username": "test",
            "password": "string",
        }
    )

    # print(response.json())

    assert response.status_code == 200
    assert response.json() == json.dumps({"message":"Invalid user login"})


# Tesing the login function
# invalid inputs: password
def test_user_login_fail1():
    response = client.post(
        "/user/login",
        json={
            "username": "Peter",
            "password": "pass",
        }
    )

    # print(response.json())

    assert response.status_code == 200
    assert response.json() == json.dumps({"message":"Invalid user login"})

