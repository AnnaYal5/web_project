from pydantic import BaseModel, EmailStr
from typing import Annotated
from pydantic import StringConstraints

class User(BaseModel):
    username: str
    password: Annotated[str, StringConstraints(min_length=8)]
    email: EmailStr

    # disabled: bool | None = None

class Ad(BaseModel):
    title: str
    description: str
    price: float
    category: str
    user: str
#
# class UserInDB(User):
#     hashed_password: str
