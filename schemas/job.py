from typing import List, Optional, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, EmailStr

from schemas.job_skill import JobSkill

class Job(BaseModel):
    id : Optional[UUID] = uuid4()
    positionName : str
    salary : int
    currency : str
    link : str
    requestedSkills: Union[List[JobSkill], None] = None
    company_id : UUID

    class Config:
        orm_mode = True
