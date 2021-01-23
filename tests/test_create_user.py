from . import client
import json

def test_user_registration_pass1():
    response = client.post(
        "/user/register",
        json={
            "username": "P",
            "password": "string",
            "age": 15,
            "gender": "male"
        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"user_id": 1, "message": "Successful user registration"}
    )

def test_create_post():
    response = client.post(
        "/create/post",
        json={
            "user_id": 1,
            "heading": "the test heading",
            "body": "the Successful test"

        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"post_id":1 , "heading": "the test heading","body": "the Successful test",}
    )



#the test should due to inernal server error as user_id=0 doesnt exist
def test_wont_create_post():
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
