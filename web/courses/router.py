from fastapi import APIRouter, Depends, Query
from typing import List, Sequence 
from typing_extensions import Annotated

# from auth.scheme import get_bearer_token

from web.courses.schemas import CourseSchema, NewCourseSchema
from web.courses.dao import CourseLectorsDAO, CoursesDAO
from web.users.dependencies import get_current_user
from web.users.models import UserModel


router = APIRouter(
    prefix="/courses",
    tags=["Курсы"]
)

# @router.get("")
# #async def get_all_users(filter_q: Annotated[UserSearch, Query()]) -> Sequence[User] | User:
# async def get_all_courses(filter_q: Annotated[CourseSearchSchema, Query()], token = Depends(get_bearer_token)) -> Sequence[CourseSchema] | CourseSchema:
#     """Получить информацию обо всех курсах
    
#     """
#     filtered = filter_q.model_dump(exclude_unset=True, exclude_defaults=True)
#     if filtered:
#         return await CourseDAO.find_all(**filtered)
#     else:
#         return await CourseDAO.find_all() 
    


@router.post("/add", status_code=201)
async def add_course(course_data: NewCourseSchema):
    """Добавить новый курс
    
    """
    await CoursesDAO.add(**course_data.model_dump())

@router.post("/add_lector", status_code=201)
async def add_lector_to_course(
    course_id: int,
    lector_id: int
    # user: UserModel = Depends(get_current_user),
    ):
    await CourseLectorsDAO.add_lector(course_id=course_id, lector_id=lector_id)


@router.get("/get_my_courses")
async def get_courses_by_lector(user: UserModel = Depends(get_current_user)):
    return await CourseLectorsDAO.get_courses_by_lector(user.id)
    

@router.delete("/")
async def del_course(ids: Annotated[List[int], Query(description="Идентификатор(ы) курса")]):
    """Удалить курс
    
    """
    return await CoursesDAO.del_by_id(ids)


@router.get("")
async def get_all_courses_info() -> Sequence[CourseSchema]:
    """
    Получить информацию о курсах
    """
    return await CoursesDAO.find_all()    


@router.get("/{id}")
async def get_course_info(id: int) -> CourseSchema:
    """Получить информацию о курсе
    
    """
    return await CoursesDAO.find_by_id(id)    