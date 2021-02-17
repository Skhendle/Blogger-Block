from pydantic import BaseModel
from typing import List, Optional


class UserRegistrationModel(BaseModel):
    username: str
    password: str
    age: int
    gender: str
