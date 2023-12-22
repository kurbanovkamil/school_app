from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(BaseModel):
    password: str


class LoginData(BaseModel):
    login: str
    password: str


class User(BaseModel):
    position: str
    login: str
    password: str
    power_level: int 


class Student(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    grade: str


class Teacher(BaseModel):
    teacher_id: int
    first_name: str
    last_name: str
    subject: str


class Class(BaseModel):
    class_name: str
    teacher_id: int


class Subject(BaseModel):
    subject_name: str


class Grade(BaseModel):
    student_id: int
    subject_id: int
    grade_value: float