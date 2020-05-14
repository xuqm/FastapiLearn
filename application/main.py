# coding=utf-8
"""
@author: xuqm
@contact: xuqinmin12@sina.com
@file: main.py
@time: 2020/5/14 14:20
@desc:
"""
from pydantic import BaseModel

from application import app


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/item_id")
def update_item(item_id: int, item: Item, ):
    return {"item_name": item.name, "item_id": item_id, }
