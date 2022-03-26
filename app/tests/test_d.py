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

    assert response.status_code == 201
    assert response.json() == {"message": "Freindship Request Sent"}

    # Peter -> Antony
    response = client.post(
        "/user/requests",
        json={
            "by_id": 1,
            "for_id": 3,
        }
    )
    assert response.status_code == 201
    assert response.json() == {"message": "Freindship Request Sent"}


    # Antony -> John
    response = client.post(
        "/user/requests",
        json={
            "by_id": 3,
            "for_id": 2,
        }
    )

    assert response.status_code == 201
    assert response.json() == {"message": "Freindship Request Sent"}


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

    assert response.status_code == 401
    assert response.json()['detail'] == 'Freind Request Already Sent'

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
    assert response.status_code == 401
    assert response.json()['detail'] == 'Freind Request Already Sent'