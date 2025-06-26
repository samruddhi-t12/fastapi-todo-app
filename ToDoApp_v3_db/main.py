from fastapi import FastAPI 
from .database import init_db
from .routes import router as task_router 

app=FastAPI()

@app.on_event("startup")
def on_startup():
	init_db()

app.include_router(task_router)