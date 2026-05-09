from fastapi import FastAPI
from pydantic import BaseModel



class User(BaseModel):
    username:str
    email:str
    age:int
    password:str



app = FastAPI()

@app.post("/register/")
async def register(user:User):
    response = {}
    if user.age < 18:
        response.update(
                {"error":"You must be 18+"}
                )
    else:
        response.update({
            "username":user.username,
            "email":user.email,
            "status":"registered"
            })

    return response


                





