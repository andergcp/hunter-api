from sqlalchemy.orm import Session

from .. import models
from ..schemas import job

def get_job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

def get_jobs(db: Session):
    return db.query(models.Job).all()

def create_job(db: Session, job: job.Job):
    new_job = models.Job(**job.dict())
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job