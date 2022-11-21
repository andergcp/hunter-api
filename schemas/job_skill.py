from typing import Optional
from pydantic import BaseModel

class JobSkill(BaseModel):
    id: Optional[str] = None
    name : str
    yearsOfExperienceRequired : int
    job_id : str

    class Config:
        orm_mode = True

class JobSkillUpdate(BaseModel):
    id: Optional[str] = None
    name : Optional[str]
    yearsOfExperienceRequired : Optional[int]
    job_id : Optional[str]

