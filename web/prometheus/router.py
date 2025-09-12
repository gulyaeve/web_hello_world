from fastapi import APIRouter


router = APIRouter(
    prefix="/prometheus",
    tags=["Мониторинг"]
)

