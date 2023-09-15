# created generate get , post , update request

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    price: float
    isOffer: Union[bool, None] = None


app = FastAPI()

@app.get("/")
def readUser():
    return {"Name": "Created by NHKHAN.."}


@app.get("/items/{item_id}")
def getUserWithId(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/{item_id}" )
def createUser(item: Item, q: Union[str, None] = None):
    return {"body":item.name, "price": item.price}

@app.put("/items/{item_id}" )
def update(item: Item, q: Union[str, None] = None):
    return {"body":item.name, "price": item.price}

print("Workinggookk indexxxxxxxxxx")