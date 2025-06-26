from fastapi import APIRouter,Depends,HTTPException 
from sqlmodel import Session,select
from .models import Task, TaskCreate, TaskRead
from .database import get_session
from .crud import create_task,get_all_tasks,get_task_by_id,update_task,delete_task
from typing import List 
from fastapi.responses import JSONResponse

router=APIRouter()

@router.get("/tasks",response_model=List[Task])
def read_tasks(session:Session=Depends(get_session)):
	return get_all_tasks(session)

@router.post("/tasks", response_model=TaskRead)
def create_new_task(task: TaskCreate, session: Session = Depends(get_session)):
	# Check if task with same name already exists
	existing = session.exec(select(Task).where(Task.name == task.name)).first()
	if existing:
		raise HTTPException(status_code=400, detail="Task with this name already exists.")
	db_task = Task.from_orm(task)
	return create_task(session, db_task)


@router.get("/tasks/{task_id}",response_model=Task)
def read_task(task_id:int,session:Session=Depends(get_session)):
	task=get_task_by_id(session,task_id)
	if not task:
		raise HTTPException(status_code=401,detail="Task Not Found")
	return task

@router.put("/tasks/{task_id}",response_model=TaskRead)
def update_existing_task(task_id:int,updated_task:TaskCreate,session:Session=Depends(get_session)):
	task=update_task(session,task_id,updated_task)
	if not task:
		raise HTTPException(status_code=404,detail="Task not found")
	return task


@router.delete("/tasks/{task_id}")
def delete_existing_task(task_id: int, session: Session = Depends(get_session)):
    task = delete_task(session, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return JSONResponse(content={"detail": "Task deleted successfully."})
