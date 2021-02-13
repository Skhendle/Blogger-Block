from pydantic import BaseModel, validator
from typing import List, Optional


class FriendRequestModel(BaseModel):
    by_id: int
    for_id: int