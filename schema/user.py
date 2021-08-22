from pydantic.main import BaseModel


class User(BaseModel):
    user_name: str
    email: str

    class Config:
        orm_mode = True


class UserCreateDto(BaseModel):
    user_name: str
    email: str
