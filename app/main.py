import json, logging
from fastapi import Depends, FastAPI
from app.dependencies import get_query_token, get_token_header
from app.routes import user_login, user_registration

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(user_login.router)
app.include_router(user_registration.router)

logging.basicConfig(filename='server.log', encoding='utf-8', level=logging.DEBUG)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

"""
    To create virtual environment $: python -m venv env
    To activate virtual environment $: source ".\env\Scripts\activate"
    To install the requirements wee run $: pip  install -r app\requirements.txt
    To update requirements.txt after new pip install use $: pip freeze > requirements.txt
    To run  the program use the following command $: hypercorn app.main:app --reload
    To deactivate virtual enviroment $: deactivate
"""