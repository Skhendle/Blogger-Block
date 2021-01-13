import json
from app.data_models.database_models import session
from app.data_models.validator_models.post import CreatePostModel
from app.data_models.database_models.post import Post
from app.data_models.database_models.user import User


class CreatePost:

    def __init__(self, inputs: CreatePostModel):
        self.__inputs = inputs

    def create_post(self):
        #check if the user exists
        user = session.query(User).filter_by(id = self.__inputs.user_id).one()
        if user :
            post = Post(
                    user_id=self.__inputs.user_id,
                    heading=self.__inputs.heading,
                    body=self.__inputs.body,
                )

            session.add(post)
            try:
                session.commit()
                return json.dumps({"post_id":post.id , "heading":post.heading,"body":post.body})
            except Exception as error:
                return json.dumps({"message":"post not created"})
        else:
            return json.dumps({"meassage":"user not valid"})
