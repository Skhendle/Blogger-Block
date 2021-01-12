import json
from app.data_models.database_models import session
from app.data_models.validator_models.post import CreatePostModel
from app.data_models.database_models.post import Post


class CreatePost:

    # inputs is validator type
    def __init__(self, inputs: CreatePostModel):
        self.__inputs = inputs

    def create_post(self):

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
            # Used to handle the registration of a user that is already in the database
            # print(error)
            return json.dumps({"message":"post not created"})
