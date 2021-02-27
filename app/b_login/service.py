from app.x_db_models import session, User

from app.b_login.input import UserLoginModel

# 
from app.e_get_friends.service import UserFriends


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
            return {'status':'failed','message':'Invalid Login'}
        
        if user.password != self.__inputs.password:
            return {'status':'failed','message':'Invalid Login'}
        

        response = {}
        response['status'] = "pass"
        response['id'] = user.id
        response['name'] = user.name 
        response['age'] = int(user.age)
        response['gender'] = user.gender


        return response
