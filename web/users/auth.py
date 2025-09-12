import logging
from passlib.context import CryptContext
from pydantic import EmailStr
from jose import jwt
from datetime import datetime, timedelta

from web.users.dao import UsersDAO
from web.exceptions import IncorrectEmailOrPassword
from web.settings import settings



pwd_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


async def auth_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        logging.warning(f"Wrong Email or Password for user {user}")
        raise IncorrectEmailOrPassword
    return user


def create_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        settings.ALGORITHM,
    )
    return encoded_jwt




if __name__ == "__main__":
    ...
    # h = get_password_hash("Start123")
    # verify = verify_password("Start1234", h)
    # print(verify)
    # from asyncio import run
    # run(auth_user("vasya@example.com", "Start123"))
    # print(create_token({"test": 1}))