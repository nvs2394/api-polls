from services.user import add_user, get_list_users, get_user_by_email
from schema.poll import Poll
from schema.user import User, UserCreateDto
from fastapi.exceptions import HTTPException
from db.db import SessionLocal, engine
from typing import List
from fastapi import status, FastAPI
from fastapi.param_functions import Depends
from sqlalchemy.orm.session import Session
from db.models import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"Hello": "World"}

# TODO: continue with CRUD poll


@app.get("/polls")
def get_polls():
    return {"polls": ""}


@app.post("/polls")
def create_poll(poll: Poll):
    return {"polls": ""}


@app.get("/users", response_model=List[User])
def get_users(skip: int = 0, limit=100, db: Session = Depends(get_db)):
    users = get_list_users(db, skip, limit)
    return users


@app.post("/users")
def create_user(user: UserCreateDto, db: Session = Depends(get_db)):
    existingUser = get_user_by_email(db, user.email)
    print('existingUser', existingUser)
    if existingUser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    return add_user(db, user)
