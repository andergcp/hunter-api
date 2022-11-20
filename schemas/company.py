from typing import List, Optional, Union
from uuid import uuid4, UUID
from pydantic import BaseModel, EmailStr

from schemas.job import Job

class Company(BaseModel):
    id : Optional[UUID] = uuid4()
    name : str
    nit : int
    city : str
    industry : str
    jobs : Union[List[Job], None] = None

    class Config:
        orm_mode = True