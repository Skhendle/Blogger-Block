import json

from app.data_models.database_models import session
from app.data_models.validator_models.user import UserLoginModel, UserRegistrationModel

from app.data_models.database_models.user import User


class UserRegistration:

    # inputs is validator type
    def __init__(self, inputs: UserRegistrationModel):
        self.__inputs = inputs


    def register_user(self):

        user = User(
                username=self.__inputs.username, 
                password=self.__inputs.password, 
                age=self.__inputs.age, 
                gender=self.__inputs.gender
            )
        
        session.add(user)
        try:
            session.commit()
            return json.dumps({"user_id":user.id ,"message":"Successful user registration"})
        except Exception as error:
            session.rollback()
            # Used to handle the registration of a user that is already in the database
            # print(error)
            return json.dumps({"message":"Invalid user registration"})

