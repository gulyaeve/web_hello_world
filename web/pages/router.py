from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from web.courses.models import CourseModel
from web.courses.router import get_all_courses_info


router = APIRouter(
    prefix="/pages",
    tags=["Фронтенд"]
)

templates = Jinja2Templates(
    directory="web/templates"
)


@router.get("/courses", response_class=HTMLResponse)
async def get_courses(
    request: Request,
    courses: CourseModel=Depends(get_all_courses_info)
    ):
    return templates.TemplateResponse(
        request=request,
        name="courses/courses.html",
        context={"courses": courses}
        )


@router.get("/login", response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", {"request": request})
