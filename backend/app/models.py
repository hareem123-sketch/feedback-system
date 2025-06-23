# backend/app/models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)  # "manager" or "employee"
    manager_id = Column(Integer, ForeignKey("users.id"), nullable=True)

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("users.id"))
    manager_id = Column(Integer, ForeignKey("users.id"))
    strengths = Column(Text)
    improvements = Column(Text)
    sentiment = Column(String)
    acknowledged = Column(Boolean, default=False)
