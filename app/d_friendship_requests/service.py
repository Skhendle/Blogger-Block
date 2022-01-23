import imp
from fastapi.responses import JSonResponse

from fastapi import HTTPException

from app.x_db_models import session, User, Requests



from app.d_friendship_requests.input import FriendRequestModel

from app.e_get_friends.service import UserFriends

class FriendRequest:

    # inputs is validator type
    def __init__(self, request: FriendRequestModel):
        self.__request = request

    def create_friendship(self):

        if self.__check_if_relationship_exist() == False:

            relation = Requests( by_id = self.__request.by_id, 
                for_id = self.__request.for_id)

            session.add(relation)

            try: 
                session.commit()
                return JSonResponse(status_code=201, content={"message":"Freindship Successfully Created"})
                
            except Exception as error:
                # Executes  when user.by_id, has relation with user.for_id
 
                session.rollback()
                return HTTPException(status_code=401, detail="Freind Request Failed")

        return  HTTPException(status_code=401, detail="Freind Request Failed") 


    def __check_if_relationship_exist(self):
        # checks if there is no request between users
        # initiated by user.for_id.

        relation = session.query(Requests).filter( 
            Requests.by_id == self.__request.for_id,
            Requests.for_id == self.__request.by_id
            ).first()

        if relation is None:
            return False
        
        return True
