import imp
from app.db_models import session, User

from app.features.b_login.input import UserLoginModel
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class UserLogin:

    # inputs is validator type
    def __init__(self, inputs: UserLoginModel):
        self.__inputs = inputs
        

    def user_login(self):
        # Can we use graphene to  data query here?
        # the excpected response is the one in
        # the Relationships Model diagram
        user = session.query(User).filter_by(
            name = self.__inputs.username,
        ).first()

        if user == None:
            raise HTTPException(status_code=400, detail='Invalid Login')
        
        if user.password != self.__inputs.password:
           raise HTTPException(status_code=401, detail='Invalid Login')
       

        response = {}
        response['message'] = "Successful Login"
        response['user_data'] = {
            'id': int(user.id),
            'username': user.name,
            'age': int(user.age),
            'gender': user.gender
        }


        return JSONResponse(status_code=201, content=response)
