from datetime import datetime
from fastapi import APIRouter

from web.users.schemas import User, UserReg
from web.users.dao import UsersDAO


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("/{id}")
def get_user_info(id: int) -> User:
    user_data = User(
        name=f"vasya_{id}",
        surname=f"ivanov_{id}",
        patronymic=None,
        login=f"ivanovv_{id}",
        # login=None,
        date_reg=datetime(2024, 9, 8, 14, 55)
    )
    # return {"user_id": id, "user_name": "vasya"}
    return user_data


@router.post("/register")
async def register_user(user_data: UserReg):
    await UsersDAO.add(**user_data.model_dump())
    print(f"User saved to db: {user_data}")
    # return user_data