from sqlmodel import SQLModel,Field 
from typing import Optional 
from datetime import date
from enum import Enum

class Priority (str,Enum):
	low="low"
	medium="medium"
	high="high"

class TaskBase(SQLModel):
	name: str
	description: Optional[str] = None
	priority: Priority = Priority.medium
	end_date: Optional[date] = None

class Task(TaskBase, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)

class TaskCreate(TaskBase):
	pass

class TaskRead(TaskBase):
	id: int

class Config:
	orm_mode = True 