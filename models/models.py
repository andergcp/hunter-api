from uuid import UUID, uuid4
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = Column(String(32))
    last_name = Column(String(32))
    email = Column(String(128))
    yearsOfPreviousExperience = Column(Integer)
    skills = relationship('UserSkill', cascade='all, delete, delete-orphan')

class UserSkill(Base):
    __tablename__ = "user_skills"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(32))
    yearsOfExperience = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))

class Job(Base):
    __tablename__ = "jobs"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4) 
    positionName = Column(String(128))
    salary = Column(Integer)
    currency = Column(String(3))
    link = Column(String)
    requestedSkills = relationship('JobSkill', cascade='all, delete, delete-orphan')
    company_id = Column(Integer, ForeignKey("company.id"))

class JobSkill(Base):
    __tablename__ = "job_skills"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(32))
    yearsOfExperienceRequired = Column(Integer)
    job_id = Column(Integer, ForeignKey("job.id"))

class Company(Base):
    __tablename__ = "companies"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(128))
    nit = Column(Integer)
    city = Column(String(128))
    industry = Column(String(128))
    jobs = relationship('Job', cascade='all, delete, delete-orphan')