from pydantic import BaseModel, validator
from typing import List, Optional


class CreatePostModel(BaseModel):
    user_id: int
    heading: str
    body: str

    @validator("heading", pre=True, always=True)
    def check_heading(cls, heading):
        assert len(heading)>0, "heading cannot be empty"
        return heading

    @validator("body", pre=True, always=True)
    def check_body(cls, body):
        assert len(body) > 0, "body cannot be empty"
        return body
