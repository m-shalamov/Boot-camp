from typing import List
import motor.motor_asyncio

from bson.objectid import ObjectId

MONGO_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.students
student_collection = database.get_collection("student_collection")


def helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "fullname": student["fullname"],
        "email": student["email"],
        "course_of_study": student["course_of_study"],
        "year": student["year"],
        "GPA": student["gpa"],
    }


async def retrieve_students() -> list:
    students = []
    async for student in student_collection.find():
        students.append(helper(student))
    return students


async def add_student_db(student_data: dict) -> dict:
    student = await student_collection.insert_one(student_data)
    new_student = await student_collection.find_one({"_id": student.inserted_id})
    return helper(new_student)
