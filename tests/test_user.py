from . import client
import json

#testing the main page
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Welcome To"}


#testing user regitration will valid details
def test_user_registration_pass():
    response = client.post(
        "/user/register",
        json={
            "username": "test_user",
            "password": "pass123",
            "age": 15,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"user_id": 1, "message": "Successful user registration"}
    )


#testing user regitration with invalid details
# repeating the user name
def test_user_registration_fail():
    response = client.post(
        "/user/register",
        json={
            "username": "test_user",
            "password": "pass123",
            "age": 15,
            "gender": "male"
        }
    )
    
    assert response.status_code == 200
    assert response.json() == json.dumps({"message": "Invalid user registration"})
    

# Tesing the login function
# valid inputs
def test_user_login_pass():
    response = client.post(
        "/user/login",
        json={
            "username": "test_user",
            "password": "pass123",
        }
    )
    
    # print(response.json())
    
    assert response.status_code == 200
    assert response.json() == {'gender': 'male', 'password': 'pass123', 'id': 1, 'age': 15, 'username': 'test_user'}


# Tesing the login function
# invalid inputs: username
def test_user_login_fail0():
    response = client.post(
        "/user/login",
        json={
            "username": "test",
            "password": "pass123",
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
            "username": "test_user",
            "password": "pass",
        }
    )
    
    # print(response.json())
    
    assert response.status_code == 200
    assert response.json() == json.dumps({"message":"Invalid user login"})
