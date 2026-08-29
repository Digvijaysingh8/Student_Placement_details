from fastapi import FastAPI, HTTPException
from schema import Student
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json


app = FastAPI()


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# Home page
@app.get("/")
def home():
    return FileResponse("static/index.html")


# Get all students
@app.get("/get_student")
def get_all_students():

    db = json.load(
        open("student_data.json", "r", encoding="utf-8-sig")
    )

    return db


# Get one student using roll number
@app.get("/get_student/{roll}")
def get_student_roll(roll: int):

    db = json.load(
        open("student_data.json", "r", encoding="utf-8-sig")
    )

    if str(roll) not in db:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return db[str(roll)]


# Add student
@app.post("/add_student")
def add_student(obj: Student):

    db = json.load(
        open("student_data.json", "r", encoding="utf-8-sig")
    )

    # Optional: prevent duplicate roll number
    if str(obj.roll) in db:
        raise HTTPException(
            status_code=400,
            detail="Roll number already exists"
        )

    db[str(obj.roll)] = {
        "Name": obj.name,
        "Marks": obj.marks,
        "Address": obj.address,
        "Placed": obj.placed
    }

    json.dump(
        db,
        open("student_data.json", "w"),
        indent=4
    )

    return {
        "message": "Student added successfully"
    }


# Delete student
@app.delete("/delete_student/{roll}")
def delete_student(roll: int):

    db = json.load(
        open("student_data.json", "r", encoding="utf-8-sig")
    )

    if str(roll) not in db:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    record = db.pop(str(roll))

    json.dump(
        db,
        open("student_data.json", "w"),
        indent=4
    )

    return {
        "message": "Student deleted successfully",
        "Deleted Record": record
    }


# Update student
@app.put("/edit_student/{roll}")
def edit_student(roll: int, obj: Student):

    db = json.load(
        open("student_data.json", "r", encoding="utf-8-sig")
    )

    # Check whether student exists
    if str(roll) not in db:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Update the existing student
    db[str(roll)] = {
        "Name": obj.name,
        "Marks": obj.marks,
        "Address": obj.address,
        "Placed": obj.placed
    }

    json.dump(
        db,
        open("student_data.json", "w"),
        indent=4
    )

    return {
        "message": "Student updated successfully"
    }