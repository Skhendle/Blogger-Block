import json
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from ..dependencies import get_token_header


class RegisterUserModel(BaseModel):
    name: str
    password: str
    age: str
    gender: str

class PostUserModel(BaseModel):
    user_id: int
    heading: str
    body: str
    
    
router = APIRouter()


@router.post("/user/register", tags=["user"])
async def register_api(user: RegisterUserModel):
    return {"A":"a","B":"b"}