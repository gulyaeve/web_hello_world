from sqlalchemy import insert, select
from web.dao.base import BaseDAO
from web.courses.models import CourseLectors, CourseModel

from web.database import async_session_maker
from web.exceptions import CourseNotPresent, UserNotPresent
from web.users.models import UserModel


class CoursesDAO(BaseDAO):
    model = CourseModel

class CourseLectorsDAO(BaseDAO):
    model = CourseLectors

    @classmethod
    async def add_lector(cls, course_id: int, lector_id: int):
        async with async_session_maker() as session:
            course_query = select(CourseModel).filter_by(id=course_id)
            result = await session.execute(course_query)
            if not result.scalar_one_or_none():
                raise CourseNotPresent
            
            user_query = select(UserModel).filter_by(id=lector_id)
            result = await session.execute(user_query)
            if not result.scalar_one_or_none():
                raise UserNotPresent
            
            query = insert(cls.model).values(course_id=course_id, user_id=lector_id)
            await session.execute(query)
            await session.commit()

    """
    WITH lector AS (SELECT public.users.id, public.users.name, public.users.surname FROM public.users WHERE id = 11) 
    SELECT * FROM public.course_lectors 
    LEFT JOIN lector on lector.id = public.course_lectors.user_id
    WHERE public.course_lectors.user_id = lector.id
    """

    @classmethod
    async def get_courses_by_lector(cls, lector_id: int):
        async with async_session_maker() as session:
            lector = select(UserModel.id, UserModel.name, UserModel.surname).where(UserModel.id == lector_id).cte("lector")
            courses_left = select(CourseLectors).join(
                lector, CourseLectors.user_id == lector.c.id, isouter=True
            ).select_from(CourseLectors).where(
                CourseLectors.user_id == lector.c.id
            ).select_from(CourseModel).join(
                CourseModel, CourseModel.id == CourseLectors.course_id, isouter=True
            )
            # ).select_from(UserModel).group_by(
            #     UserModel.id, UserModel.name, UserModel.surname, CourseLectors.course_id, CourseLectors.user_id
            # )
            result = await session.execute(courses_left)
            return result.scalars().all()

            
    