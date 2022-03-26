from pydantic import BaseModel
from typing import List, Optional


class UserLoginModel(BaseModel):
    username: str
    password: str