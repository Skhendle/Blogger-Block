from fastapi import APIRouter, Depends


from app.a_login.input import UserLoginModel
from app.a_login.service import UserLogin

router = APIRouter()


@router.post("/user/login", tags=["user"])
async def login_api(user: UserLoginModel):
    return UserLogin(user).user_login()