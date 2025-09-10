from typing import Optional
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from web.exceptions import TokenMissing
from web.settings import settings


# Тут должно быть получение токена из БД
known_tokens = {
    settings.TOKEN_BEARER,
    }


async def get_bearer_token(
        auth: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error=False))
    ) -> str:
    if auth is None or (token := auth.credentials) not in known_tokens:
        raise TokenMissing
    return token