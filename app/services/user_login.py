import json

from app.data_models.database_models import session
from app.data_models.validator_models.user import UserLoginModel

from app.data_models.database_models.user import User

from app.services.get_friends import UserFriends


class UserLogin:

    # inputs is validator type
    def __init__(self, inputs: UserLoginModel):
        self.__inputs = inputs

        

    def user_login(self):

        try:
            # Can we use graphene to  data query here?
            # the excpected response is the one in
            # the Relationships Model diagram
            user = session.query(User).filter_by(
                    name = self.__inputs.username,
                    password = self.__inputs.password
                ).first()
            
            response = {}
            response['id'] = user.id
            response['name'] = user.name 
            response['age'] = user.age
            response['gender'] = user.gender

            response['posts'] = []
            for post in user.posts:
                response['posts'].append({
                    'id': post.id,
                    'heading':post.heading,
                    'body':post.body
                })


            response['friends'] = UserFriends(user=user).get_friends()
            # UserFriends(user=user).friends()
            return response
        except Exception as error:
            session.rollback()
            print(error)
            return json.dumps({"message":"Invalid user login"})