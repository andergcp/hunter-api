from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from models import app_models
from schemas import company, job, job_skill, user, user_skill
from views import company_view, job_skills_view, job_view, user_skills_view, user_view
from database import SessionLocal, engine

app_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Users operations
@app.post("/users/", response_model=user.User)
def create_user(user: user.User, db: Session = Depends(get_db)):
    return user_view.create_user(db=db, user=user)


@app.get("/users/", response_model=List[user.User])
def read_users( db: Session = Depends(get_db)):
    users = user_view.get_users(db)
    return users


@app.get("/users/{user_id}", response_model=user.User)
def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = user_view.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: str, db: Session = Depends(get_db)):
    user_deletion = user_view.delete_user(db, user_id=user_id)
    if user_deletion["status_code"] == 400:
        raise HTTPException(status_code=400, detail=user_deletion["message"])
    return user_deletion["message"]

@app.put("/users/{user_id}")
def update_user(userNewData: user.UserUpdate, user_id: str, db: Session = Depends(get_db)):
    stored_user = user_view.get_user(db, user_id=user_id)
    stored_user_model = user.User(**stored_user.__dict__)
    update_data = userNewData.dict(exclude_unset=True)
    updated_user = stored_user_model.copy(update=update_data)
    user_update_result = user_view.update_user(db, user_id=user_id, updatedUser=updated_user)
    return user_update_result

# Companies operations
@app.post("/companies/", response_model=company.Company)
def create_company(company: company.Company, db: Session = Depends(get_db)):
    return company_view.create_company(db=db, company=company)


@app.get("/companies/", response_model=List[company.Company])
def read_companies( db: Session = Depends(get_db)):
    companies = company_view.get_companies(db)
    return companies


@app.get("/companies/{company_id}", response_model=company.Company)
def read_company(company_id: str, db: Session = Depends(get_db)):
    db_company = company_view.get_company(db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company

@app.delete("/companies/{company_id}")
def delete_company(company_id: str, db: Session = Depends(get_db)):
    company_deletion = company_view.delete_company(db, company_id=company_id)
    if company_deletion["status_code"] == 400:
        raise HTTPException(status_code=400, detail=company_deletion["message"])
    return company_deletion["message"]

@app.put("/companies/{company_id}")
def update_company(companyNewData: company.CompanyUpdate, company_id: str, db: Session = Depends(get_db)):
    stored_company = company_view.get_company(db, company_id=company_id)
    stored_company_model = company.Company(**stored_company.__dict__)

    update_data = companyNewData.dict(exclude_unset=True)
    updated_company = stored_company_model.copy(update=update_data)

    company_update_result = company_view.update_company(db, company_id=company_id, updatedCompany=updated_company)
    return company_update_result

# Jobs operations
@app.post("/jobs/", response_model=job.Job)
def create_job(job: job.Job, db: Session = Depends(get_db)):
    return job_view.create_job(db=db, job=job)


@app.get("/jobs/", response_model=List[job.Job])
def read_jobs( db: Session = Depends(get_db)):
    jobs = job_view.get_jobs(db)
    return jobs


@app.get("/jobs/{job_id}", response_model=job.Job)
def read_job(job_id: str, db: Session = Depends(get_db)):
    db_job = job_view.get_job(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job

@app.delete("/jobs/{job_id}")
def delete_job(job_id: str, db: Session = Depends(get_db)):
    job_deletion = job_view.delete_job(db, job_id=job_id)
    if job_deletion["status_code"] == 400:
        raise HTTPException(status_code=400, detail=job_deletion["message"])
    return job_deletion["message"]

@app.put("/jobs/{job_id}")
def update_job(jobNewData: job.JobUpdate, job_id: str, db: Session = Depends(get_db)):
    stored_job = job_view.get_job(db, job_id=job_id)
    stored_job_model = job.Job(**stored_job.__dict__)
    update_data = jobNewData.dict(exclude_unset=True)
    updated_job = stored_job_model.copy(update=update_data)
    job_update_result = job_view.update_job(db, job_id=job_id, updatedJob=updated_job)
    return job_update_result

# User Skills operations
@app.post("/user_skills/", response_model=user_skill.UserSkill)
def create_user_skill(userSkill: user_skill.UserSkill, db: Session = Depends(get_db)):
    return user_skills_view.create_user_skill(db=db, userSkill=userSkill)

@app.get("/user_skills/{user_skill_id}", response_model=user_skill.UserSkill)
def read_user_skill(user_skill_id: str, db: Session = Depends(get_db)):
    db_user_skill = user_skills_view.get_user_skill(db, user_skill_id=user_skill_id)
    if db_user_skill is None:
        raise HTTPException(status_code=404, detail="La habilidad que buscas no existe")
    return db_user_skill

@app.delete("/user_skills/{user_skill_id}")
def delete_user_skill(user_skill_id: str, db: Session = Depends(get_db)):
    user_skill_deletion = user_skills_view.delete_user_skill(db, user_skill_id=user_skill_id)
    if user_skill_deletion["status_code"] == 400:
        raise HTTPException(status_code=400, detail=user_skill_deletion["message"])
    return user_skill_deletion["message"]

@app.put("/user_skills/{user_skill_id}")
def update_user_skill(userSkillNewData: user_skill.UserSkillUpdate, user_skill_id: str, db: Session = Depends(get_db)):
    stored_user_skill = user_skills_view.get_user_skill(db, user_skill_id=user_skill_id)
    stored_user_skill_model = user_skill.UserSkill(**stored_user_skill.__dict__)

    update_data = userSkillNewData.dict(exclude_unset=True)
    updated_user_skill = stored_user_skill_model.copy(update=update_data)

    user_skill_update_result = user_skills_view.update_user_skill(db, user_skill_id=user_skill_id, updatedUserSkill=updated_user_skill)
    return user_skill_update_result

# Job Skills operations
@app.post("/job_skills/", response_model=job_skill.JobSkill)
def create_job_skill(jobSkill: job_skill.JobSkill, db: Session = Depends(get_db)):
    return job_skills_view.create_job_skill(db=db, jobSkill=jobSkill)

@app.get("/job_skills/{job_skill_id}", response_model=job_skill.JobSkill)
def read_job_skill(job_skill_id: str, db: Session = Depends(get_db)):
    db_job_skill = job_skills_view.get_job_skill(db, job_skill_id=job_skill_id)
    if db_job_skill is None:
        raise HTTPException(status_code=404, detail="La habilidad que buscas no existe")
    return db_job_skill

@app.delete("/job_skills/{job_skill_id}")
def delete_job_skill(job_skill_id: str, db: Session = Depends(get_db)):
    job_skill_deletion = job_skills_view.delete_job_skill(db, job_skill_id=job_skill_id)
    if job_skill_deletion["status_code"] == 400:
        raise HTTPException(status_code=400, detail=job_skill_deletion["message"])
    return job_skill_deletion["message"]

@app.put("/job_skills/{job_skill_id}")
def update_job_skill(jobSkillNewData: job_skill.JobSkillUpdate, job_skill_id: str, db: Session = Depends(get_db)):
    stored_job_skill = job_skills_view.get_job_skill(db, job_skill_id=job_skill_id)
    stored_job_skill_model = job_skill.JobSkill(**stored_job_skill.__dict__)

    update_data = jobSkillNewData.dict(exclude_unset=True)
    updated_job_skill = stored_job_skill_model.copy(update=update_data)

    job_skill_update_result = job_skills_view.update_job_skill(db, job_skill_id=job_skill_id, updatedJobSkill=updated_job_skill)
    return job_skill_update_result
    
#General Root

@app.get("/")
def read_root():
    return {"Hello": "World"}