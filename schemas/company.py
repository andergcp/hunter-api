from typing import List, Optional, Union
from pydantic import BaseModel

from schemas.job import Job

class Company(BaseModel):
    id: Optional[str] = None
    name : str
    nit : int
    city : str
    industry : str
    jobs : Union[List[Job], None] = None

    class Config:
        orm_mode = True

class CompanyUpdate(BaseModel):
    id: Optional[str] = None
    name : Optional[str]
    nit : Optional[int]
    city : Optional[str]
    industry : Optional[str]

