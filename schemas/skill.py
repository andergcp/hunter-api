from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel

class Skill(BaseModel):
    id: Optional[UUID] = uuid4()
    name : str
    yearsOfExperience : int
