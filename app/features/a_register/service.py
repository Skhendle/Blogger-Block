import json
import sqlite3
from app.features.a_register.input import UserRegistrationModel
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from app.db_models import session, User
class UserRegistration:

    # inputs is validator type
    def __init__(self, inputs: UserRegistrationModel):
        self.__inputs = inputs


    def register_user(self):

        user = User(
                name=self.__inputs.username, 
                password=self.__inputs.password, 

                age=self.__inputs.age, 
                gender=self.__inputs.gender
            )
        
        session.add(user)
        
        try:
            session.commit()
            return JSONResponse(status_code=201, content={"message":"Successful Registration"})
        except Exception as error:
            session.rollback()
            raise HTTPException(status_code=401, detail="Invalid Registration")
