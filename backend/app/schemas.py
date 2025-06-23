from pydantic import BaseModel

class FeedbackBase(BaseModel):
    manager_id: int
    employee_id: int
    strengths: str
    improvements: str
    sentiment: str

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackOut(FeedbackBase):
    id: int
    acknowledged: bool

    class Config:
        orm_mode = True
