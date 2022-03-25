from fastapi import APIRouter, Depends


from app.features.e_get_friends.service import UserFriends

router = APIRouter()


@router.get("/friends/{user_id}", tags=["user"])
async def friends_api(user_id: int):
    return UserFriends(user_id=user_id).get_friends()