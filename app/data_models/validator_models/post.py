from pydantic import BaseModel
from typing import List, Optional


class PostModel(BaseModel):
    user_id: int
    heading: str
    body: str
