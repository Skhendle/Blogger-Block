import json
import sqlite3
from app.a_register.input import UserRegistrationModel


from app.x_db_models import session, User
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
            return {"status": "pass", "message":"Successful registration"}
        except Exception as error:
            session.rollback()
            return {"status": "fail", "message":"Invalid Registration"}
