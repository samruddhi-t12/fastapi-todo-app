
from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import date
from enum import Enum

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class Task(BaseModel):
    id:int
    name: str = Field(..., min_length=2, max_length=30)
    description: Optional[str] = None
    priority: Priority = Priority.medium
    end_date: Optional[date] = None

    @validator("end_date")
    def check_date(cls, v):
        if v is not None and v < date.today():
            raise ValueError("Date shouldn't be in past")
        return v






	
	


