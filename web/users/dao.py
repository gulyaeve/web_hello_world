from web.dao.base import BaseDAO
from web.users.models import UserModel


class UsersDAO(BaseDAO):
    model = UserModel
    