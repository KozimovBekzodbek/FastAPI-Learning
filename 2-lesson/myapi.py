from enum import Enum
from fastapi import FastAPI

class ModelName(str, Enum):
    quyosh = 'quyosh'
    oy = 'oy'
    yulduz = 'yulduz'


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/items/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}



@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
    if model_name is ModelName.quyosh:
        return {"model_name":model_name, "message":"Quyosh ham katta bir yulduz"}

    if model_name.value == "oy":
        return {"model_name":model_name, "message":"Oy Yer sayyorasining yo'ldoshi"}


    if model_name is ModelName.yulduz:
        return {"model_name":model_name, "message":"Yulduz bu gallaktikadagi bir yorug' jism"}

    return {"model_name":model_name, "message": f"{model_name} bu nomda model mavjud emas"}






@app.get("/files/{file_path:path}")
async def get_files(file_path: str):
    return {"file_path":file_path}

