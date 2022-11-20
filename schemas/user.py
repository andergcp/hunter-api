from typing import List, Optional, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, EmailStr

from schemas.skill import Skill

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    email : EmailStr
    yearsOfPreviousExperience : int
    skills : Union[List[Skill], None] = None