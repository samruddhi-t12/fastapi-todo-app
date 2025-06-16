# FastAPI ToDo App (Structured Version) 🗂️

This is the **structured version** of my FastAPI ToDo backend API project.  
Built to implement best practices in project organization, routing, and data validation with Pydantic.

---

## 🚀 Features

- Modular structure using `main.py`, `models.py`, and `routes.py`
- Add, view, update, and delete tasks
- Filter tasks by priority using query parameters
- Input validation using Pydantic models
- Custom validator to prevent past-due end dates

---

## 🛠 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Run the app:
   ```bash
   uvicorn ToDoApp_V1.main:app --reload
3. Open in browser:
  
    Swagger UI: http://127.0.0.1:8000/docs

---

## 🧱 Folder Structure

ToDoApp_V2/

├── main.py         # Entry point with FastAPI app instance

├── routes.py       # API route definitions

├── models.py       # Pydantic models and schema

├── __init__.py     # Makes it a Python package

└── requirements.txt

---

## 📌Concepts Covered

- REST API design with FastAPI
- Project structuring and routing
- Request body validation with Pydantic
- Enum usage and optional fields
- Custom error handling and validators
- Query parameters

---

## 🧰Tech Stack

- FastAPI
- Python 3.10+
- Pydantic
- Uvicorn

---

## 👩‍💻 Author
Samruddhi Thorat
