from fastapi import APIRouter, Depends
from app.data_models.validator_models.user import UserRegistrationModel
from app.services.user_registration import UserRegistration    

router = APIRouter()


@router.post("/user/register", tags=["user"])
async def register_api(user: UserRegistrationModel):
    return UserRegistration(user).register_user()