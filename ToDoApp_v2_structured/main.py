from fastapi import FastAPI
from ToDoApp_V2.routes import router as todo_router
app=FastAPI()

app.include_router(todo_router,prefix="/todos",tags=["ToDos"])

@app.get("/")
def home():
	return{"message":"Welcome to the Modular ToDo App!"}

if __name__ =="__main__":
	import uvicorn 
	uvicorn.run("ToDoApp_V1.main:app",host="127.0.0.1",port=8000,reload=True)