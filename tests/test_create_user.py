from . import client
import json



def test_create_post():
    response = client.post(
        "/create/post",
        json={
            "user_id": 1,
            "heading": "the test heading",
            "body": "the Successful test",

        }
    )

    assert response.status_code == 200
    assert response.json() == json.dumps(
        {"user_id":1 , "heading": "the test heading","body": "the Successful test",}
    )

#the test should due to inernal server error as user_id=0 doesnt exist
def test_wont_create_post():
    response = client.post(
        "/create/post",
        json={
            "user_id": 0,
            "heading": "the test heading",
            "body": "the Successful test",

        }
    )

    assert response.status_code == 500
    assert response.json() == json.dumps(
    "Internal Server Error"
    )
