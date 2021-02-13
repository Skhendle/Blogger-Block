import json, logging
from fastapi import Depends, FastAPI

from app.c_create_post import route

app = FastAPI()


app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "This is the create post service"}
