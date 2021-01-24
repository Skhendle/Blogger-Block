import json

from app.data_models.database_models import session


from app.data_models.database_models.user import User
from app.data_models.database_models.requests import Requests



class UserFriends:

    # inputs is validator type
    def __init__(self, user: User):
        self.__user = user

    def get_friends(self):
        friends = []
        friends.extend(self.__requests_received())

        friends.extend(self.__requests_sent())
        return friends


    # Uses the 'friends' attribute(from User object). To get 
    # id of User objects that sent friend requests to 'user'
    def __requests_received(self):
        items = []

        for  friend_assoc in self.__user.friends:

            # Getting the friend from the user table,  Indexing - primary key
            friend = session.query(User).filter( User.id == friend_assoc.by_id).first()
            a = {
                'id': str(friend_assoc.by_id),
                'friend name': str(friend.name),
                'age': str(friend.age),
                'gender': str(friend.gender),
                'request':'received',
                'posts': []
            }

            for post in friend.posts:
                b = {
                    'id': post.id,
                    'heading':  post.heading,
                    'body':post.body,
                    'date': post.date
                }
                a['posts'].append(b)
            
            items.append(a)
            

        return items


    def __requests_sent(self):

        items = []

        # Using the request association table, to get User objects
		# that received friend requests from 'user'.
        # Indexing - primary key
        receiver = session.query(Requests).filter( Requests.by_id == self.__user.id)
        for friend in receiver:
            a = {
                'id': str(friend.for_id),
                'name': str(friend.friends.name),
                'age': str(friend.friends.age),
                'gender': str(friend.friends.gender),
                'request':'sent',
                'posts': []
            }

            for post in friend.friends.posts:
                b = {
                    'id': post.id,
                    'heading':  post.heading,
                    'body':post.body,
                    'date': post.date
                }
                a['posts'].append(b)
            
            items.append(a)

        return items
