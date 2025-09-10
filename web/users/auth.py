from passlib.context import CryptContext
from pydantic import EmailStr

from web.users.dao import UsersDAO
from web.exceptions import IncorrectEmailOrPassword



pwd_context = CryptContext(schemes=["md5_crypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


async def auth_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one(email=email)
    if not (user and verify_password(password, user.hashed_password)):
        raise IncorrectEmailOrPassword
    return user




if __name__ == "__main__":
    ...
    # h = get_password_hash("Start123")
    # verify = verify_password("Start1234", h)
    # print(verify)
    # from asyncio import run
    # run(auth_user("vasya@example.com", "Start123"))