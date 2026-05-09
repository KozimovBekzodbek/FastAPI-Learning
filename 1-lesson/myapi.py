from fastapi import FastAPI, Path


app = FastAPI()

students = {
        1:{
            "name":"Bekzodbek",
            "age" : 21,
            "address": "Andijon"
           },
        
        2:{
            "name":"Lola",
            "age" : 20,
            "address": "Andijon"
            }

        }



@app.get("/")
def root():
    return {"name":"Bekzodbek"}



@app.get("/students/")
def students_list():
    return students


@app.get("/students/{student_id}/")
def students_detail(student_id: int):
    student = students.get(int(student_id), "Ololmadim")
    return {"message":student}


 
@app.get("/students/{name}")
def student_get_by_name(name):
    for student in students:
        if students[student]["name"]  == name:
            return students[student]
        return f"'{name}' bu nomda o'quvchi mavjud emas."






