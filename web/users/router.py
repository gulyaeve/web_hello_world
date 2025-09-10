from typing import Sequence, Annotated
from fastapi import APIRouter, Depends, Query, Response

from web.users.auth import auth_user, get_password_hash, create_token
from web.users.dependencies import get_current_user
from web.users.models import UserModel
from web.users.schemas import UserScheme, UserReg, UserSearch, UserLogin
from web.users.dao import UsersDAO
from web.exceptions import UserExistException


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("")
async def get_all_users(filter_query: Annotated[UserSearch, Query()]) -> Sequence[UserScheme]:
    """
    Get all users
    """
    filter_model = filter_query.model_dump(exclude_unset=True, exclude_defaults=True)
    return await UsersDAO.find_all(**filter_model)


# @router.get("")
# async def get_all_users_2(filter_query: Annotated[UserSearch, Query()]) -> Sequence[User] | User:
#     """
#     Get all users with single model
#     """
#     filter_model = filter_query.model_dump(exclude_unset=True, exclude_defaults=True)
#     return await UsersDAO.find(**filter_model)


@router.post("/register", status_code=201)
async def register_user(user_data: UserReg):
    existing_user = await UsersDAO.find_one(email=user_data.email)
    if existing_user:
        raise UserExistException
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        email=user_data.email,
        name=user_data.name,
        surname=user_data.surname,
        hashed_password=hashed_password,
    )
    print(f"User saved to db: {user_data}")
    # return user_data


@router.post("/login")
async def login_user(response: Response, user_data: UserLogin):
    user = await auth_user(user_data.email, user_data.password)
    access_token = create_token({"sub": str(user.id)})
    response.set_cookie("access_token", access_token)
    return {"access_token": access_token}


@router.get("/me")
async def user_get_itself(current_user: UserModel = Depends(get_current_user)) -> UserScheme:
    return current_user
    


@router.get("/{id}")
async def get_user_info(id: int) -> UserScheme:
    return await UsersDAO.find_by_id(id)