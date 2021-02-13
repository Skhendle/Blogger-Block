from fastapi import APIRouter, Depends


from app.b_register.input import UserRegistrationModel
from app.b_register.service import UserRegistration    

router = APIRouter()



@router.post("/user/register", tags=["user"])
async def register_api(user: UserRegistrationModel):
    return UserRegistration(user).register_user()