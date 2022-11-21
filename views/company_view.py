from models import app_models

from sqlalchemy.orm import Session

import schemas.company
import uuid

def get_company(db: Session, company_id: str):
    # stored_company_in_db = db.query(app_models.Company).filter(app_models.Company.id == company_id).first()
    return db.query(app_models.Company).filter(app_models.Company.id == company_id).first()

def get_companies(db: Session):
    return db.query(app_models.Company).all()

def create_company(db: Session, company: schemas.company.Company):
    if company.id is None:
        company.id = str(uuid.uuid4())

    new_company = app_models.Company(**company.dict())
    db.add(new_company)
    db.commit()
    return new_company

def delete_company(db: Session, company_id: str):
    company = db.query(app_models.Company).filter(app_models.Company.id == company_id).first()
    if company is None:
        return {"message":"La empresa que quieres borrar no existe", "status_code": 400}
    db.delete(company)
    db.commit()
    return {"message":"Empresa borrada exitosamente", "status_code": 204}

def update_company(db: Session, company_id: str, updatedCompany: schemas.company.Company):
    company = db.query(app_models.Company).filter(app_models.Company.id == company_id).first()

    updatedCompany.jobs = db.query(app_models.Job).filter(app_models.Job.company_id == company_id).all()
    if updatedCompany.jobs is None:
        updatedCompany.jobs = []
    
    updatedCompanyDict = updatedCompany.dict()
    for key, value in updatedCompanyDict.items():
            setattr(company, key, value)
            
    db.add(company)
    db.commit()
    db.refresh(company)
    return company