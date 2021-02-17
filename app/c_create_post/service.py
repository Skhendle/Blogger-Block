from app.x_db_models import session, User, Post
from app.c_create_post.input import CreatePostModel


class CreatePost:

    def __init__(self, inputs: CreatePostModel):
        self.__inputs = inputs

    def create_post(self):
        # check if the user exists
        try:
            user = session.query(User).filter_by(id = self.__inputs.user_id).one()
            if user :
                post = Post(
                    user_id=self.__inputs.user_id,
                    heading=self.__inputs.heading,
                    body=self.__inputs.body
                )

                session.add(post)
                session.commit()
                return {"post_id":post.id , "heading":post.heading,"body":post.body}

        except Exception as error:
            session.rollback()
            return {'status':'failed', 'message': 'invalid post creation'}
