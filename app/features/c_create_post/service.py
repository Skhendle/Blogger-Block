import imp
from app.db_models import session, User, Post
from app.features.c_create_post.input import CreatePostModel
from fastapi.responses import JSONResponse
from fastapi import HTTPException

class CreatePost:

    def __init__(self, inputs: CreatePostModel):
        self._inputs = inputs

    def create_post(self):
        # check if the user exists
        try:
            user = session.query(User).filter_by(id = self._inputs.user_id).one()
            if user :
                post = Post(
                    user_id=self._inputs.user_id,
                    heading=self._inputs.heading,
                    body=self._inputs.body
                )

                session.add(post)
                session.commit()
                return JSONResponse(status_code=201, content ={"post_id":post.id , "heading":post.heading,"body":post.body})

        except Exception as error:
            session.rollback()
            raise HTTPException(status_code= 401, detail ='Invalid Post Creation')
