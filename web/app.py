from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from sqladmin import Admin

from web.admin.views import UsersAdmin
from web.admin.auth import authentication_backend
from web.auth.scheme import get_bearer_token
from web.users.router import router as users_router
from web.courses.router import router as courses_router
from web.images.router import router as images_router
from web.database import engine
from web.settings import settings
from random import randint
from time import sleep
from asyncio import sleep as asleep
from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(settings.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield


app = FastAPI(lifespan=lifespan)


# SECURITY = [Depends(get_bearer_token)]

# app.include_router(users_router, dependencies=SECURITY)
app.include_router(users_router)
app.include_router(courses_router)
app.include_router(images_router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test_sync/{id}")
def test_sync(id: int):
    time_to_wait = randint(3, 10)
    print(f"Получен {id}, будет выполнена за {time_to_wait} секунд")
    sleep(time_to_wait)
    print(f"Задача {id} завершена" )
    return {"msg": f"Задача {id} завершена за {time_to_wait} секунд"}


@app.get("/test_async/{id}")
async def test_async(id: int):
    time_to_wait = randint(3, 10)
    print(f"Получен {id}, будет выполнена за {time_to_wait} секунд")
    asleep(time_to_wait)
    print(f"Задача {id} завершена" )
    return {"msg": f"Задача {id} завершена за {time_to_wait} секунд"}


admin = Admin(app, engine, authentication_backend=authentication_backend)
admin.add_view(UsersAdmin)
