from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel

class JobSkill(BaseModel):
    id: Optional[UUID] = uuid4()
    name : str
    yearsOfExperienceRequired : int
    job_id : UUID

    class Config:
        orm_mode = True
