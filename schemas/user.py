from typing import List, Optional, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, EmailStr

from schemas.user_skill import UserSkill

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    email : EmailStr
    yearsOfPreviousExperience : int
    skills : Union[List[UserSkill], None] = None
    
    class Config:
        orm_mode = True