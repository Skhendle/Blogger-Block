import json

from app.data_models.database_models import session
from app.data_models.validator_models.user import UserLoginModel

from app.data_models.database_models.user import User


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
                    username = self.__inputs.username,
                    password = self.__inputs.password
                ).one()
            # print(user)
            return user
        except Exception as error:
            session.rollback()
            # print(error)
            return json.dumps({"message":"Invalid user login"})