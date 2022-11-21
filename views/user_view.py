from models import app_models

from sqlalchemy.orm import Session

import schemas.user
import uuid

def get_user(db: Session, user_id: int):
    return db.query(app_models.User).filter(app_models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(app_models.User).all()

def create_user(db: Session, user: schemas.user.User):
    if user.id is None:
        user.id = str(uuid.uuid4())
    new_user = app_models.User(**user.dict())
    db.add(new_user)
    db.commit()
    return new_user

def delete_user(db: Session, user_id: str):
    user = db.query(app_models.User).filter(app_models.User.id == user_id).first()
    if user is None:
        return {"message":"El usuario que quieres borrar no existe", "status_code": 400}
    db.delete(user)
    db.commit()
    return {"message":"Usuario borrado exitosamente", "status_code": 204}

def update_user(db: Session, user_id: str, updatedUser: schemas.user.User):
    user = db.query(app_models.User).filter(app_models.User.id == user_id).first()

    updatedUser.skills = db.query(app_models.UserSkill).filter(app_models.UserSkill.user_id == user_id).all()
    if updatedUser.skills is None:
        updatedUser.skills = []
    
    updatedUserDict = updatedUser.dict()
    for key, value in updatedUserDict.items():
            setattr(user, key, value)

    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_recomendations(db: Session, user_id: str):
    user_skills = db.query(app_models.UserSkill).filter(app_models.UserSkill.user_id == user_id).all()

    jobs = db.query(app_models.Job).all()

    recommendedJobs = []
    for job in jobs:
        if isMatch(job, user_skills):
            recommendedJobs.append(job)
    
    return recommendedJobs
        

def isMatch(job: app_models.Job, user_skills: app_models.UserSkill):
    requiredSkills = job.requestedSkills
    numberRequestedSkills = len(requiredSkills)
    matchingSkills = 0

    for rs in requiredSkills:
        for us in user_skills:
            if rs.name == us.name and rs.yearsOfExperienceRequired <= us.yearsOfExperience:
                matchingSkills += 1

    if matchingSkills >= numberRequestedSkills/2:
        return True
    return False