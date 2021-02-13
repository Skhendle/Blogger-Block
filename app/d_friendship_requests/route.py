from fastapi import APIRouter, Depends

from app.d_friendship_requests.input import FriendRequestModel

from app.d_friendship_requests.service import FriendRequest    


router = APIRouter()


@router.post("/user/requests", tags=["user"])
async def friend_request_api(input: FriendRequestModel):
    return FriendRequest(input).create_friendship()