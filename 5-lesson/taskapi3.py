from fastapi import FastAPI
from pydantic import BaseModel



class User(BaseModel):
    username:str
    password:str





app = FastAPI()


@app.post("/login")
async def login(user:User):
    if user.username == "admin" and user.password == "1234":
        return {"message":"Successfully"}
    else:
        return {"message":"Error occured"}



