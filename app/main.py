import json, logging
from fastapi import Depends, FastAPI

from app.routes import user_login, user_registration , create_post, friend_requests

app = FastAPI()


app.include_router(user_login.router)
app.include_router(user_registration.router)
app.include_router(create_post.router)
app.include_router(friend_requests.router)


@app.get("/")
async def root():
    return {"message": "Hello Welcome To"}
