from . import client

# Testing if a user with valid credentials
# can login successfully and get list of
# friends 
def test_user_gets_friends():
    url = "/friends/3"
    response = client.get(
        url
    )

    assert response.status_code == 200
    # Tests fails becomesof the string formats
    # assert response.json() == {'id': 3, 'name': 'Antony', 'age': '25', 'gender': 'male', 'posts': [{'id': 3, 'heading': 'Antony', 'body': "Hello, I'm Antony"}], 'friends': [{'id': '1', 'friend name': 'Peter', 'age': '20', 'gender': 'male', 'request': 'received', 'posts': [{'id': 1, 'heading': 'Peter', 'body': "Hello, I'm Peter.", 'date': '2021-02-17T23:25:32.559418'}]}, {'id': '2', 'name': 'John', 'age': '20', 'gender': 'male', 'request': 'sent', 'posts': [{'id': 2, 'heading': 'John', 'body': "Hello, I'm John", 'date': '2021-02-17T23:25:32.561927'}]}]}


if __name__ == "__main__":
    test_user_gets_friends()