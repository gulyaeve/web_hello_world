from fastapi import APIRouter, Depends, UploadFile

from web.images.publish import publish_image_to_queue
from web.users.dependencies import get_current_user
from web.users.models import UserModel

from shutil import copyfileobj
from os.path import abspath


router = APIRouter(
    prefix="/images",
    tags=["Загрузка картинок"]
)


@router.post("/avatars")
async def add_user_avatar(file: UploadFile, current_user: UserModel = Depends(get_current_user)):
    # image_path = join("C:\\Users\\Admin\\static\\", f"{current_user.id}.webp")
    image_path = f"web/static/images/{current_user.id}.webp"
    image_abs_path = abspath(image_path)
    with open(image_path, "+bw") as file_object:
        copyfileobj(file.file, file_object)

    data = {
        "user_id": current_user.id,
        "img_path": image_abs_path
    }

    await publish_image_to_queue(data)