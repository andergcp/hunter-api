from models import app_models

from sqlalchemy.orm import Session

import schemas.job_skill
import uuid

def get_job_skill(db: Session, job_skill_id: str):
    # stored_job_skill_in_db = db.query(app_models.JobSkill).filter(app_models.JobSkill.id == job_skill_id).first()
    return db.query(app_models.JobSkill).filter(app_models.JobSkill.id == job_skill_id).first()
    
def create_job_skill(db: Session, jobSkill: schemas.job_skill.JobSkill):
    if jobSkill.id is None:
        jobSkill.id = str(uuid.uuid4())

    new_job_skill = app_models.JobSkill(**jobSkill.dict())
    db.add(new_job_skill)
    db.commit()
    return new_job_skill

def delete_job_skill(db: Session, job_skill_id: str):
    job_skill = db.query(app_models.JobSkill).filter(app_models.JobSkill.id == job_skill_id).first()
    if job_skill is None:
        return {"message":"La habilidad que quieres borrar no existe", "status_code": 400}
    db.delete(job_skill)
    db.commit()
    return {"message":"Habilidad borrada exitosamente", "status_code": 204}

def update_job_skill(db: Session, job_skill_id: str, updatedJobSkill: schemas.job_skill.JobSkillUpdate):
    job_skill = db.query(app_models.JobSkill).filter(app_models.JobSkill.id == job_skill_id).first()
    updatedJobSkillDict = updatedJobSkill.dict()
    print(updatedJobSkillDict)
    for key, value in updatedJobSkillDict.items():
            setattr(job_skill, key, value)
    print(job_skill.__dict__)        
    db.add(job_skill)
    db.commit()
    db.refresh(job_skill)
    return job_skill