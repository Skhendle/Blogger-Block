from . import client

# Testing if a user can successfully create a post
def test_create_post_pass():
    response = client.post(
        "/create/post",
        json={
            "user_id": 1,
            "heading": "Peter",
            "body": "Hello, I'm Peter."
        }
    )

    assert response.status_code == 201
    assert response.json() == {"post_id":1 , "heading": "Peter","body": "Hello, I'm Peter."}

    response = client.post(
        "/create/post",
        json={
            "user_id": 2,
            "heading": "John",
            "body": "Hello, I'm John"
        }
    )
    assert response.status_code == 201
    assert response.json() == {"post_id":2 , "heading": "John","body": "Hello, I'm John"}


    response = client.post(
        "/create/post",
        json={
            "user_id": 3,
            "heading": "Antony",
            "body": "Hello, I'm Antony"
        }
    )
    assert response.status_code == 201
    assert response.json() == {"post_id":3 , "heading": "Antony","body": "Hello, I'm Antony"}



def test_create_post_fail():

    # Invalid user id
    response = client.post(
        "/create/post",
        json={
            "user_id": 100,
            "heading": "the test heading",
            "body": "the Successful test"

        }
    )

    assert response.status_code == 401
    assert response.json()['detail'] == 'Invalid Post Creation'