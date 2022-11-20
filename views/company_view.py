from sqlalchemy.orm import Session

from .. import models
from ..schemas import company

def get_company(db: Session, company_id: int):
    return db.query(models.Company).filter(models.Company.id == company_id).first()

def get_companies(db: Session):
    return db.query(models.Company).all()

def create_company(db: Session, company: company.Company):
    new_company = models.Company(**company.dict())
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company