import json

from app.data_models.database_models import session


from app.data_models.database_models.user import User
from app.data_models.database_models.requests import Requests

from app.data_models.validator_models.friendship_request import FriendRequestModel

from app.services.get_friends import UserFriends

class FriendRequest:

    # inputs is validator type
    def __init__(self, request: FriendRequestModel):
        self.__request = request

    def create_friendship(self):

        if self.__check_if_relationship_exist() == True:


            relation = Requests(by_id=self.__request.by_id,
                for_id=self.__request.for_id)

            session.add(relation)

            try: 
                session.commit()
                return "friendship successfully created"
            except Exception as error:
                session.rollback()
                return "friend request failed"

        return "friend request failed"

    def __check_if_relationship_exist(self):

        relation = session.query(Requests).filter( 
            Requests.by_id == self.__request.for_id,
            Requests.for_id == self.__request.by_id
            ).first()

        if relation is  None:
            return True
        
        return False
