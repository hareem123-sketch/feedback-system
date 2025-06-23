# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS setup (important to allow frontend access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class Feedback(BaseModel):
    id: int
    manager_id: int
    employee_id: int
    strengths: str
    improvements: str
    sentiment: str
    acknowledged: bool = False

class FeedbackCreate(BaseModel):
    manager_id: int
    employee_id: int
    strengths: str
    improvements: str
    sentiment: str

# In-memory "database"
feedback_list: List[Feedback] = []
next_id = 1

# Routes
@app.post("/feedback/")
def create_feedback(feedback: FeedbackCreate):
    global next_id
    new_feedback = Feedback(id=next_id, **feedback.dict())
    feedback_list.append(new_feedback)
    next_id += 1
    return new_feedback
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/feedback/{employee_id}")
def get_feedback_for_employee(employee_id: int):
    return [f for f in feedback_list if f.employee_id == employee_id]

@app.get("/feedbacks/manager/{manager_id}")
def get_feedback_for_manager(manager_id: int):
    return [f for f in feedback_list if f.manager_id == manager_id]

@app.post("/feedback/{feedback_id}/acknowledge")
def acknowledge_feedback(feedback_id: int):
    for f in feedback_list:
        if f.id == feedback_id:
            f.acknowledged = True
            return {"message": "Acknowledged"}
    raise HTTPException(status_code=404, detail="Feedback not found")
