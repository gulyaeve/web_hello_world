from datetime import datetime
from typing import Sequence
from fastapi import APIRouter

from web.users.schemas import User, UserReg
from web.users.dao import UsersDAO
from web.exceptions import UserExistException


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{id}")
async def get_user_info(id: int) -> User:
    return await UsersDAO.find_by_id(id)


@router.get("")
async def get_all_users() -> Sequence[User]:
    """
    Get all users
    """
    return await UsersDAO.find_all()


@router.post("/register", status_code=201)
async def register_user(user_data: UserReg):
    existing_user = UsersDAO.find_one(email=user_data.email)
    if existing_user:
        raise UserExistException
    await UsersDAO.add(**user_data.model_dump())
    print(f"User saved to db: {user_data}")
    # return user_data