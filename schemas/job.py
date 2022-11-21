from typing import List, Optional, Union
from pydantic import BaseModel

from schemas.job_skill import JobSkill

class Job(BaseModel):
    id : Optional[str] = None
    positionName : str
    salary : int
    currency : str
    link : str
    requestedSkills: Union[List[JobSkill], None] = None
    company_id : str

    class Config:
        orm_mode = True

class JobUpdate(BaseModel):
    id : Optional[str] = None
    positionName : Optional[str]
    salary : Optional[int]
    currency : Optional[str]
    link : Optional[str]
    company_id : Optional[str]