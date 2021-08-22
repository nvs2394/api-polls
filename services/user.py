from schema.user import UserCreateDto
from sqlalchemy.orm import session
from db.models.models import User
from db.db import SessionLocal


def get_list_users(db: SessionLocal, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: session, email: str):
    print('get_user_by_email', email)
    return db.query(User).filter(User.email == email).first()


def add_user(db: session.Session, userCreateDto: UserCreateDto):
    new_user = User(email=userCreateDto.email,
                    user_name=userCreateDto.user_name)
    print('new_user', new_user)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
