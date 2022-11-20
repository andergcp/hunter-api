from typing import Optional
from uuid import uuid4, UUID
from pydantic import BaseModel

class UserSkill(BaseModel):
    id: Optional[UUID] = uuid4()
    name : str
    yearsOfExperience : int
    user_id : UUID

    class Config:
        orm_mode = True