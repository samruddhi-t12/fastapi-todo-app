from fastapi import FastAPI,Query,HTTPException
from pydantic import BaseModel,Field
from typing import Optional,List  #data validation library 
from datetime import date
from enum import Enum

app=FastAPI() #creating object of class FastAPI
#In memory storage 
todo_list:List["ToDoItem"]=[]

class Priority(str,Enum):
	low="low"
	medium="medium"
	high="high"
#Data Model
class ToDoItem(BaseModel):
	id : int
	task: str=Field(...,min_length=1,max_length=100)
	description: str | None=None
	completed: bool =False
	priority: Priority=Priority.medium
	end_date: Optional[date]=None
#Routes
@app.get("/")
def read_root():
	return{"message": "Welcome to your ToDo app!"}

@app.get("/todos")
def get_todods(completed: Optional[bool]=Query(None,description="Filter by completion status (true/false)")):
	if completed is None:
		return todo_list
	filtered=[todo for todo in todo_list if todo.completed==completed]
	return{"filtered_todos" : filtered}

@app.get("/todos/{item_id}")
def get_todo_by_id(item_id:int):
	for todo in todo_list:
		if todo.id==item_id:
			return todo
	raise HTTPException(status_code=404,detail="ToDo not found")



@app.post("/todos")
def add_todo(item: ToDoItem):
	todo_list.append(item)
	return{"message":"ToDo added successfully" ,"todo" : item.model_dump()}

@app.put("/todos/{item_id}")
def update_todo(item_id:int,updated_item:ToDoItem):
	for i,todo in enumerate(todo_list):
		if todo.id==item_id:
			todo_list[i]=updated_item
			return {"message":"ToDo updated","todo":updated_item.model_dump()}
	raise HTTPException(status_code=404,detail="Todo not found")

@app.delete("/todos/{item_id}")
def delete_todo(item_id:int):
	for i,todo in enumerate(todo_list):
		if todo.id==item_id:
			deleted = todo_list.pop(i)
			return{"message": "ToDo deleted","todo" :deleted.model_dump()}
	raise HTTPException(status_code=404,detail="Todo not found")

