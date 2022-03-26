import json, logging
from fastapi import Depends, FastAPI

# from app.routes import user_login, user_registration , create_post, friend_requests

app = FastAPI()

from app.features.a_register import route
app.include_router(route.router)

from app.features.b_login import route
app.include_router(route.router)

from app.features.c_create_post import route
app.include_router(route.router)

from app.features.d_friendship_requests import route
app.include_router(route.router)

# from app.features.e_get_friends import route
# app.include_router(route.router)

@app.get("/")
async def root():
    return {"message": "The Entire Application"}