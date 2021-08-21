from fastapi import FastAPI
from pydantic import BaseModel
import enum

app = FastAPI()


class User(BaseModel):
    user_name: str
    email: str


class Poll(BaseModel):
    title: str
    type: str
    created_by: str
    is_add_choices_active: bool
    is_voting_active: bool


@app.get("/")
def root():
    return {"Hello": "World"}


@app.get("/polls")
def get_polls():
    return {"polls": ""}


@app.post("/polls")
def create_poll(poll: Poll):
    return {"polls": ""}


@app.get("/users")
def get_users():
    return {"users": ""}


@app.post("/users")
def create_user(user: User):
    return {"users": ''}
