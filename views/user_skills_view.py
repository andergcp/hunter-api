from models import app_models

from sqlalchemy.orm import Session

import schemas.user_skill
import uuid

def get_user_skill(db: Session, user_skill_id: str):
    # stored_user_skill_in_db = db.query(app_models.UserSkill).filter(app_models.UserSkill.id == user_skill_id).first()
    return db.query(app_models.UserSkill).filter(app_models.UserSkill.id == user_skill_id).first()
    
def create_user_skill(db: Session, userSkill: schemas.user_skill.UserSkill):
    if userSkill.id is None:
        userSkill.id = str(uuid.uuid4())

    new_user_skill = app_models.UserSkill(**userSkill.dict())
    db.add(new_user_skill)
    db.commit()
    return new_user_skill

def delete_user_skill(db: Session, user_skill_id: str):
    user_skill = db.query(app_models.UserSkill).filter(app_models.UserSkill.id == user_skill_id).first()
    if user_skill is None:
        return {"message":"La habilidad que quieres borrar no existe", "status_code": 400}
    db.delete(user_skill)
    db.commit()
    return {"message":"Habilidad borrada exitosamente", "status_code": 204}

def update_user_skill(db: Session, user_skill_id: str, updatedUserSkill: schemas.user_skill.UserSkillUpdate):
    user_skill = db.query(app_models.UserSkill).filter(app_models.UserSkill.id == user_skill_id).first()
    
    updatedUserSkillDict = updatedUserSkill.dict()
    for key, value in updatedUserSkillDict.items():
            setattr(user_skill, key, value)
            
    db.add(user_skill)
    db.commit()
    db.refresh(user_skill)
    return user_skill