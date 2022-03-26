from fastapi import APIRouter, Depends


from app.features.b_login.input import UserLoginModel
from app.features.b_login.service import UserLogin

router = APIRouter()


@router.post("/user/login", tags=["user"])
async def login_api(user: UserLoginModel):
    return UserLogin(user).user_login()