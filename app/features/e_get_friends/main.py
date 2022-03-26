import json, logging
from fastapi import Depends, FastAPI

from app.features.e_get_friends import route

app = FastAPI()


app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "This is the login service"}
