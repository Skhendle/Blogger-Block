import imp
from fastapi.responses import JSONResponse

from fastapi import HTTPException

from app.db_models import session, User, Requests



from app.features.d_friendship_requests.input import FriendRequestModel

from app.features.e_get_friends.service import UserFriends

class FriendRequest:

    # inputs is validator type
    def __init__(self, request: FriendRequestModel):
        self.__request = request

    def create_friendship(self):

        if self._check_if_relationship_exist() == False:

            relation = Requests( by_id = self.__request.by_id, 
                for_id = self.__request.for_id, status= "Pending")
            session.add(relation)
            try: 
                session.commit()
                session.close()
                return JSONResponse(status_code=201, content={'message':'Freindship Request Sent'})
            except Exception as error:
                session.rollback()
                session.close()
                raise HTTPException(status_code=401, detail='Invalid Request, Please Try Again')

        # Executes  when user.by_id, has relation with user.for_id
        raise  HTTPException(status_code=401, detail='Freind Request Already Sent') 


    def _check_if_relationship_exist(self):
        # checks if there is no request between users
        # initiated by user.for_id.

        relation_one = session.query(Requests).filter( 
            Requests.by_id == self.__request.for_id,
            Requests.for_id == self.__request.by_id
        ).first()

        relation_two = session.query(Requests).filter( 
            Requests.by_id == self.__request.by_id,
            Requests.for_id == self.__request.for_id
        ).first()


        if relation_one == relation_two == None:
            return False
        
        return True
