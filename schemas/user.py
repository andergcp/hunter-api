from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr

from schemas.user_skill import UserSkill

class User(BaseModel):
    id: Optional[str] = None
    first_name : str
    last_name : str
    email : EmailStr
    years_of_previous_experience : int
    skills : Union[List[UserSkill], None] = None
    
    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    id: Optional[str] = None
    first_name : Optional[str]
    last_name : Optional[str]
    email : Optional[EmailStr]
    years_of_previous_experience : Optional[int]
    skills : Union[List[UserSkill], None] = None