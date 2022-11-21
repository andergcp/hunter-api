from typing import Optional
from pydantic import BaseModel

class UserSkill(BaseModel):
    id: Optional[str] = None
    name : str
    yearsOfExperience : int
    user_id : str

    class Config:
        orm_mode = True

class UserSkillUpdate(BaseModel):
    id: Optional[str] = None
    name : Optional[str]
    yearsOfExperience : Optional[int]
    user_id : Optional[str]