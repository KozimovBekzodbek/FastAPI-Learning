from fastapi import FastAPI
from pydantic import BaseModel


class Product(BaseModel):
    name:str
    price:float
    discount:int| None=None


app = FastAPI()


@app.post("/product/")
async def discount(product:Product):
    product_dict = product.model_dump()
    if product.discount is not None:
        product_dict.update(
                {"final_price":product.price - product.price*product.discount / 100}
                )
    else:
        product_dict.update(
                {"final_price":product.price, "discount":"No discount percent"}
                )


    return product_dict

