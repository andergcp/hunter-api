from typing import List, Union
from uuid import UUID, uuid4

from fastapi import FastAPI
from models.skill import Skill

from models.user import User

app = FastAPI()

db: List[User] = [
    User(
        id = UUID("fe21964b-25f3-439f-9e45-898c6338d8d4"),
        first_name = "Ander",
        last_name = "Capri",
        email = "a@a.com",
        yearsOfPreviousExperience = 5,
        skills = [Skill(name="Analityc", yearsOfExperience=8)]
    ),
    User(
        id = UUID("6ee35389-ca0f-4669-9534-1d3b2acb62b2"),
        first_name = "Ander2",
        last_name = "Capri2",
        email = "a@a2.com",
        yearsOfPreviousExperience = 4,
        skills = [Skill(name="Smart", yearsOfExperience=3), Skill(name="Kind", yearsOfExperience=2)]
    )
]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/v1/users")
def fetch_all_users():
    return db

@app.post("/api/v1/users")
def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
