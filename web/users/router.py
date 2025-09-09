from datetime import datetime
from fastapi import APIRouter

from web.users.schemas import User, UserReg
from web.users.dao import UsersDAO


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{id}")
async def get_user_info(id: int) -> User:
    return await UsersDAO.find_by_id(id)


@router.post("/register")
async def register_user(user_data: UserReg):
    await UsersDAO.add(**user_data.model_dump())
    print(f"User saved to db: {user_data}")
    # return user_data