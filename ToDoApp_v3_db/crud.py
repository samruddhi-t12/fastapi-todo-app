from sqlmodel import Session,select 
from .models import Task,TaskCreate

def create_task(session:Session,task:Task):
	session.add(task)
	session.commit()
	session.refresh(task)
	return task

def get_all_tasks(session :Session):
	return session.exec(select(Task)).all()

def get_task_by_id(session :Session,task_id:int):
	return session.get(Task,task_id)

def update_task(session:Session,task_id:int,updated_task:TaskCreate):
	existing=session.get(Task,task_id)
	if not existing :
		return None
	for attr,value in updated_task.dict(exclude_unset=True).items():
		setattr(existing,attr,value)
	session.commit()
	session.refresh(existing)
	return existing

def delete_task(session:Session,task_id:int):
	task=session.get(Task,task_id)
	if not task:
		return None
	session.delete(task)
	session.commit()
	return task


