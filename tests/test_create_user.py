from . import client
import json

def test_user_registration_pass1():

    response = client.post(
        "/user/register",
        json={
            "username": "Peter",
            "password": "string",
            "age": 20,
            "gender": "male"
        }
    )

    response = client.post(
        "/user/register",
        json={
            "username": "John",
            "password": "string",
            "age": 20,
            "gender": "male"
        }
    )
    response = client.post(
        "/user/register",
        json={
            "username": "Antony",
            "password": "string",
            "age": 25,
            "gender": "male"
        }
    )
    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"user_id": 3, "message": "Successful user registration"}
    )


#testing user regitration with invalid details
# repeating the user name
def test_user_registration_fail():
    response = client.post(
        "/user/register",
        json={
            "username": "Peter",
            "password": "pass123",
            "age": 15,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps({"message": "Invalid user registration"})


def test_post_pass():
    response = client.post(
        "/create/post",
        json={
            "user_id": 1,
            "heading": "Peter",
            "body": "the Successful test"

        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"post_id":1 , "heading": "Peter","body": "the Successful test",}
    )

    response = client.post(
        "/create/post",
        json={
            "user_id": 2,
            "heading": "John",
            "body": "the Successful test"

        }
    )

    response = client.post(
        "/create/post",
        json={
            "user_id": 3,
            "heading": "Antony",
            "body": "the Successful test"

        }
    )




# the test should fail due to an inernal server error,
#  as user_id=0 doesnt exist.
def test_post_creation_fail():
    response = client.post(
        "/create/post",
        json={
            "user_id": 100,
            "heading": "the test heading",
            "body": "the Successful test"

        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps({
    "message":"user does not exist"})


def  test_friendship_request_pass():
    response = client.post(
        "/user/requests",
        json={
            "by_id": 1,
            "for_id": 2,
        }
    )

    response = client.post(
        "/user/requests",
        json={
            "by_id": 1,
            "for_id": 3,
        }
    )

    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 2,
        }
    )

    assert response.status_code == 200
    assert response.json() == "friendship successfully created"

#repeat existing association
def  test_friendship_request_fail1():
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 2,
        }
    )

    assert response.status_code == 200
    assert( response.json() == "friend request failed")

#creating an inverted request forassociation in table
def  test_friendship_request_fail2():
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 1,
        }
    )

    assert response.status_code == 200
    assert( response.json() == "friend request failed")