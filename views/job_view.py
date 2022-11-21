from models import app_models

from sqlalchemy.orm import Session

import schemas.job
import uuid

def get_job(db: Session, job_id: int):
    return db.query(app_models.Job).filter(app_models.Job.id == job_id).first()

def get_jobs(db: Session):
    return db.query(app_models.Job).all()

def create_job(db: Session, job: schemas.job.Job):
    if job.id is None:
        job.id = str(uuid.uuid4())

    new_job = app_models.Job(**job.dict())
    db.add(new_job)
    db.commit()
    return new_job

def delete_job(db: Session, job_id: str):
    job = db.query(app_models.Job).filter(app_models.Job.id == job_id).first()
    if job is None:
        return {"message":"La vacante que quieres borrar no existe", "status_code": 400}
    db.delete(job)
    db.commit()
    return {"message":"Vacante borrada exitosamente", "status_code": 204}

def update_job(db: Session, job_id: str, updatedJob: schemas.job.Job):
    job = db.query(app_models.Job).filter(app_models.Job.id == job_id).first()

    updatedJob.requestedSkills = db.query(app_models.JobSkill).filter(app_models.JobSkill.job_id == job_id).all()
    if updatedJob.requestedSkills is None:
        updatedJob.requestedSkills = []
    
    updatedJobDict = updatedJob.dict()
    for key, value in updatedJobDict.items():
            setattr(job, key, value)
            
    db.add(job)
    db.commit()
    db.refresh(job)
    return job
