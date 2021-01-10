from fastapi import APIRouter, Depends
from app.data_models.validator_models.user import UserLoginModel
from app.services.user_login import UserLogin    

router = APIRouter()


@router.get("/user/login", tags=["user"])
async def login_api(user: UserLoginModel):
    return UserLogin(user).user_login()