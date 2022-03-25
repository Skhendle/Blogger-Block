from fastapi import APIRouter, Depends


from app.features.c_create_post.input import CreatePostModel
from app.features.c_create_post.service import CreatePost


router = APIRouter()


@router.post("/create/post", tags=["post"])
async def create_post_api(post: CreatePostModel):
    return CreatePost(post).create_post()
