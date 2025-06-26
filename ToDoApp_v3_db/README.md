# FastAPI ToDo App (Database Version) 🧩

This is the *V3 version* of my FastAPI ToDo backend API — now fully integrated with a *SQLite database* using SQLModel.  
Built with modularity, real-world structure, and database support to scale toward production-ready apps.

---

## 🚀 Features

- Modular project structure with clean separation of concerns
- CRUD operations (Create, Read, Update, Delete) with persistence
- SQLite database integration using SQLModel
- Auto-generated interactive Swagger UI
- Input validation using Pydantic
- Unique task name check to avoid duplicates
- Proper error handling and response models
- Ready to migrate to PostgreSQL or other DBs later

---

## 🛠 How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt

2. Run the app:
   - uvicorn ToDoApp_V3.main:app --reload

3. Open in browser:
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc
---

## 🧱 Folder Structure

ToDoApp_V3/


├── main.py         # Entry point with FastAPI app instance

├── models.py       # SQLModel classes and schemas

├── crud.py         # Database interaction logic (create, read, update, delete)

├── routes.py       # API route definitions and endpoints

├── database.py     # SQLite engine and session management

├── _init_.py     # Makes it a Python package

├── requirements.txt

└── README.md


---

## 📌 Concepts Covered

- SQLModel ORM integration

- Session-based database operations

- Input validation & response modeling

- Dependency injection with FastAPI

- Error handling & duplicate prevention

- RESTful design with proper structure



---

## 🧰 Tech Stack

- FastAPI

- Python 3.10+

- SQLModel

- SQLite (for now)

- Uvicorn (ASGI server)

- Pydantic



---

## 👩‍💻 Author

Samruddhi Thorat
