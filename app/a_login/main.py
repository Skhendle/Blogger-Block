import json, logging
from fastapi import Depends, FastAPI

from app.a_login import route

app = FastAPI()


app.include_router(route.router)


@app.get("/")
async def root():
    return {"message": "This is the login service"}
