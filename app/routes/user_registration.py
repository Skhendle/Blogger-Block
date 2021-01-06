import json
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from ..dependencies import get_token_header


class RegisterUserModel(BaseModel):
    name: str
    password: str
    age: str
    gender: str


router = APIRouter()


@router.post("/user/register", tags=["user"])
async def register_api(user: RegisterUserModel):
    return {"A":"a","B":"b"}