import json

from app.x_data_models.database_models import session
from app.x_data_models.database_models.user import User


from app.b_register.input import UserRegistrationModel




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
            return json.dumps({"user_id":user.id ,"message":"Successful user registration"})
        except Exception as error:
            session.rollback()
            # Used to handle the registration of a user that is already in the database
            # print(error)
            return json.dumps({"message":"Invalid user registration"})

