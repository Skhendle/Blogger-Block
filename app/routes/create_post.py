from fastapi import APIRouter, Depends
from app.data_models.validator_models.post import CreatePostModel
from app.services.create_post import CreatePost

router = APIRouter()


@router.post("/create/post", tags=["post"])
async def create_post_api(post: CreatePostModel):
    return CreatePost(post).create_post()
