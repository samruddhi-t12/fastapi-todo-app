from fastapi import APIRouter,HTTPException,Response
from typing import List,Optional 
from pydantic import BaseModel
from ToDoApp_V2.models import Task,Priority

router=APIRouter()
task_list:List[Task]=[]

class TaskResponse(BaseModel):
	message: str
	task: Task

def is_duplicate_id(task_id: int, exclude_id: int = None) -> bool:
	for task in task_list:
		if task.id==task_id and task.id!=exclude_id:
			return True
	return False

@router.get("/todo", response_model=List[Task])
def get_task(priority:Optional[Priority]=None):
	if priority:
        	return [task for task in task_list if task.priority == priority]
	return task_list

@router.post("/todo", response_model=TaskResponse)
def add_task(tsk:Task):

	if is_duplicate_id(tsk.id):
		raise HTTPException(status_code=400,detail="ID should not be repeated")
	task_list.append(tsk)
	return{"message":"Task added","task":tsk.model_dump()}

@router.put("/todo/{id}", response_model=TaskResponse)
def update_task(id:int,updated_task:Task):
	for i,item in enumerate(task_list):
		if item.id==id:
			if is_duplicate_id(updated_task.id,exclude_id=id):
				raise HTTPException(status_code=400,detail="Updated ID conflicts with another task id")
			task_list[i]=updated_task
			return{"message":"Task updated"
,"task":updated_task.model_dump()}
	raise HTTPException(status_code=404,detail="Task not found")

@router.delete("/todo/{id}", response_model=TaskResponse)
def delete_task(id:int):
	for i, item in enumerate(task_list):
		if item.id==id:
			deleted = task_list.pop(i)

			return{"message":"Task deleted","task":deleted.model_dump()}
	raise HTTPException(status_code=404,detail="Task not found")


	