from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class User(BaseModel):
    # id: int
    name: str
    surname: str
    patronymic: Optional[str]
    login: str
    date_reg: datetime
    email: Optional[EmailStr]


class UserReg(BaseModel):
    email: EmailStr
    login: str
    name: str
    surname: str
