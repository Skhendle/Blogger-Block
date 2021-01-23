from pydantic import BaseModel, validator
from typing import List, Optional


class FriendRequestModel(BaseModel):
    by_id: int
    for_id: int

    # @validator("heading", pre=True, always=True)
    # def check_by_id(cls, by_id):
    #     assert by_id !=  None, "Requester id cannot be empty"
    #     return by_id

    # @validator("body", pre=True, always=True)
    # def check_for_id(cls, for_id):
    #     assert for_id != None, "Requestee id cannot be empty"
    #     return for_id
