from fastapi import FastAPI



app = FastAPI()

fake_items_db = [{"item_name":"Telefon"}, {"item_name":"Kandisioner"}, {"item_name":"Shokolad"}, {"item_name":"Banan"}]


@app.get("/items")
async def read_items(skip: int = 0,  limit:int = 2):
    return fake_items_db[skip:limit]



@app.get("/items/{item_id}")
async def read_item(item_id:str, q:str| None=None, short:bool=False):
    item = {"item_id":item_id}
    if q:
        item.update(
                {"q":q}
                )
    if not short:
        item.update(
                {"description":"Bu fast api yordamida qilingan so'rov"}

                )

    return item 

