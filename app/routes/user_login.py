import json
from pydantic import BaseModel
from fastapi import APIRouter, Depends
from ..dependencies import get_token_header


class LoginModel(BaseModel):
    email: str
    password: str


router = APIRouter()


@router.post("/user/login", tags=["user"])
async def login_api(login_user: LoginModel):
    return {"A":"a","B":"b"}