from fastapi import Depends, FastAPI

from web.auth.scheme import get_bearer_token
from web.users.router import router as users_router
from random import randint
from time import sleep
from asyncio import sleep as asleep

app = FastAPI()

# SECURITY = [Depends(get_bearer_token)]

# app.include_router(users_router, dependencies=SECURITY)
app.include_router(users_router)


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
