from web.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship


class CourseModel(Base):
    """
    Модель [sqlalchemy] 'Курс'
    """    
    __tablename__ = "course"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(Integer, nullable=True)

    users = relationship("CourseLectors", uselist=True, backref="course")


class CourseLectors(Base):
    __tablename__ = "course_lectors"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"), primary_key=True)