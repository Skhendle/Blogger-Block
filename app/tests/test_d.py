from . import client


def  test_friendship_request_pass():
    
    # Peter -> John
    response = client.post(
        "/user/requests",
        json={
            "by_id": 1,
            "for_id": 2,
        }
    )

    # Peter -> Antony
    response = client.post(
        "/user/requests",
        json={
            "by_id": 1,
            "for_id": 3,
        }
    )

    # Antony -> John
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 2,
        }
    )

    assert response.status_code == 200
    assert response.json() == {"status": "pass", "message":"Freindship Request Successful"}


def  test_friendship_request_fail():
    # repeat existing association
    # Antony -> John
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 2,
        }
    )

    assert response.status_code == 200
    assert response.json() == {"status": "fail", "message":"Freindship Request Invalid"}

    # creating an inverted request,
    # for association in table.
    # Antony -> Peter
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 1,
        }
    )

    assert response.status_code == 200
    assert response.json() == {"status": "fail", "message":"Freindship Request Invalid"}