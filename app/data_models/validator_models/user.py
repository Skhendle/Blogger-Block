from pydantic import BaseModel
from typing import List, Optional


class UserLoginModel(BaseModel):
    username: str
    password: str


class UserRegistrationModel(BaseModel):
    username: str
    password: str
    age: int
    gender: str
