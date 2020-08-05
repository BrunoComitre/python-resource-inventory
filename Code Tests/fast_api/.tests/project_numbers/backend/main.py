from fastapi import FastAPI, HTTPException, Form, Body, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

import constants as const
from models import Notas

app = FastAPI()

# origins = [
#     "http://localhost:8000"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = origins,
#     allow_credentials = True,
#     allow_methods = ["*"],
#     allow_headers = ["*"],
# )


class Number(BaseModel):
    value: Optional[int] = None
    # name: str
    # value: int
    # description: Optional[str] = None
    # price: float
    # tax: Optional[float] = None
    # tags: list = []

numbers = Number(value=0)

class Items(BaseModel):
    items: dict

    # @classmethod
    # def as_form(
    #     cls,
    #     items: dict = Form(...)
    # ) -> Items:
    #     return cls(items=items)

items = Items(items = {})
items = const.items


@app.get("/number")
def get_number() -> Number:
    """ Return value for global variable :numbers: """
    global numbers
    return {"number": numbers.value}


@app.post("/number")
def update_number(num: Number):
    """ Altar value from global variable :number: for  :num: """
    global numbers
    numbers.value = num
    #     raise HTTPException(status_code=404, detail="Item not found")
    # else:
    return {"number": numbers.value}
 

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    global items

    return {"item": items[item_id]}


@app.post("/items/{item_id}")
# def update_item(item: Items =  Form(...)):
async def update_item(item: Items ):#= Depends(Items.as_form)):
    global items
    items[item_id].value = item
    return {"item": items[item_id].value}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     global items
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}

@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Items, embed=True):
    global items
    item_id.value = item
    results = {"item_id": item_id, "item": item}
    return results
