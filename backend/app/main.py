from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app import models, schemas

# Initialize FastAPI app
app = FastAPI()

# CORS setup
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
async def read_root():
    return {"message": "Welcome to the Feedback System API!"}

# Create feedback
@app.post("/feedback/", response_model=schemas.FeedbackOut)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = models.Feedback(**feedback.dict())
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

# Get feedback for a specific employee
@app.get("/feedback/{employee_id}", response_model=list[schemas.FeedbackOut])
def get_feedback(employee_id: int, db: Session = Depends(get_db)):
    return db.query(models.Feedback).filter(models.Feedback.employee_id == employee_id).all()

# Get feedbacks submitted by a specific manager
@app.get("/feedbacks/manager/{manager_id}", response_model=list[schemas.FeedbackOut])
def get_manager_feedback(manager_id: int, db: Session = Depends(get_db)):
    return db.query(models.Feedback).filter(models.Feedback.manager_id == manager_id).all()

# Acknowledge a specific feedback
@app.post("/feedback/{feedback_id}/acknowledge")
def acknowledge_feedback(feedback_id: int, db: Session = Depends(get_db)):
    feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if not feedback:
        raise HTTPException(status_code=404, detail="Feedback not found")
    feedback.acknowledged = True
    db.commit()
    return {"message": "Acknowledged"}
