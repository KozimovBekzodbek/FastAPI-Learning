from fastapi import FastAPI
from pydantic import BaseModel

class Student(BaseModel):
    name:str
    score:int


app = FastAPI()


@app.post("/students/{student_id}/")
def score_student(student:Student, student_id:int):
    if grade 
