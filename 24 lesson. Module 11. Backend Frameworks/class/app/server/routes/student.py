from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import add_student_db, retrieve_students
from server.models.student import StudentSchema, ResponseModel, ErrorResponseModel

router = APIRouter()


@router.get("/", response_description="Students retrieved")
async def get_students():
    students = await retrieve_students()
    if students:
        return ResponseModel(students, "Students data retrieved")
    return ErrorResponseModel("No content", 204, "Empty list")


@router.post("/", response_description="Student data added into db")
async def add_student(student: StudentSchema = Body(...)):
    student = jsonable_encoder(student)
    new_student = await add_student_db(student)
    return ResponseModel(new_student, "Student was added")
