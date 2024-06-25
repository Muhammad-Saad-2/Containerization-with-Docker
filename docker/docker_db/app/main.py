from typing import Optional
from app import settings
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlmodel import Field, SQLModel, Session, create_engine

from app.settings import DATABASE_URL, SessionLocal


# SQLAlchemy engine creation
connection_string = str(settings.DATABASE_URL).replace("postgresql", "postgresql+psycopg")
engine = create_engine(connection_string, connect_args={}, pool_recycle=300)

# Base class for SQLAlchemy models
Base = declarative_base()


# SQLModel definition for Todo table
class Todo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str = Field(index=True)


# SQLModel definition for Student table
class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    zipcode = Column(String, index=True)


# Create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)


# Pydantic model for creating a new student (input validation)
class StudentCreate(BaseModel):
    name: str
    email: str
    zipcode: str


# Pydantic model for reading a student (output validation)
class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    zipcode: str

    class Config:
        from_attributes = True  # Convert SQLAlchemy objects to dict


# FastAPI app instance
app = FastAPI()


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint to create a new student
@app.post("/students/", response_model=StudentResponse)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email, zipcode=student.zipcode)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


# Endpoint to retrieve a student by ID
@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student


# Endpoint to update a student by ID
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(student_id: int, student: StudentCreate, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db_student.name = student.name
    db_student.email = student.email
    db_student.zipcode = student.zipcode
    db.commit()
    db.refresh(db_student)
    return db_student


# Endpoint to delete a student by ID
@app.delete("/students/{student_id}", response_model=StudentResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(db_student)
    db.commit()
    return db_student
