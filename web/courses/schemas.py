from typing import Annotated, Optional

from pydantic import BaseModel, Field


class CourseSchema(BaseModel):
    """
    Модель [Pydantic] "Курс"

    """
    id:          Annotated[Optional[int], Field(description="Идентификатор", default=None)]
    name:        Annotated[Optional[str], Field(description="Название", default="CourseName")]
    description: Annotated[Optional[str], Field(description="Описание", default="CourseDesc" )]
    duration:    Annotated[Optional[int], Field(description="Продолжительность", default="")]
    # teacher_id:  Annotated[Optional[int], Field(description="Преподаватель", default="")]


class NewCourseSchema(BaseModel):
    name:        Annotated[Optional[str], Field(description="Название", default="CourseName")]
    description: Annotated[Optional[str], Field(description="Описание", default="CourseDesc" )]
    duration:    Annotated[Optional[int], Field(description="Продолжительность", default="")]