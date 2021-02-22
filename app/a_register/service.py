import json

from app.x_db_models import session,User
from app.a_register.input import UserRegistrationModel


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
            return {"user_id":user.id, "message":"Successful user registration"}
        except Exception as error:
            session.rollback()
            return {"message":"Invalid user registration"}

