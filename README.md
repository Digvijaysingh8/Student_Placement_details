# 🎓 Student Details Management System

A simple full-stack **Student Details Management System** built using **FastAPI** for the backend and **HTML, CSS, and JavaScript** for the frontend. The application allows users to add, view, edit, and delete student records through a REST API.

Student information such as **Roll Number, Name, Marks, Address, and Placement Status** is stored in a JSON file and managed through FastAPI CRUD endpoints.

---

## 🚀 Features

- ➕ Add new student
- 📋 View all students
- 🔍 Get a student using Roll Number
- ✏️ Edit student details
- 🗑️ Delete student
- 🎨 Simple and responsive frontend
- 🔄 Frontend communicates with backend using REST APIs
- 📁 JSON file used for data storage
- 📖 Interactive FastAPI Swagger documentation

---

## 🛠️ Technologies Used

### Backend
- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON

### Frontend
- HTML
- CSS
- JavaScript
- Fetch API

### Data Storage
- JSON file

---

## 📂 Project Structure

```text
Student_details_App/
│
├── main.py
├── schema.py
├── student_data.json
│
└── static/
    ├── index.html
    ├── students.html
    └── edit.html
