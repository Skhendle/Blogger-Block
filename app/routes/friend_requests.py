from fastapi import APIRouter, Depends
from app.data_models.validator_models.friendship_request import FriendRequestModel
from app.services.friendship_requests import FriendRequest    

router = APIRouter()


@router.post("/user/requests", tags=["user"])
async def friend_request_api(input: FriendRequestModel):
    return FriendRequest(input).create_friendship()