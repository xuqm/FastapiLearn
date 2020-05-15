from fastapi import Body
from pydantic import BaseModel

from part6 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    full_name: str = None


@app.put("/items1/{item_id}")
async def update_item1(*, item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


"""
{
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0
  },
  "user": {
    "username": "string",
    "full_name": "string"
  },
  "importance": 1
}
"""


# Body body参数验证
@app.put("/items2/{item_id}")
async def update_item2(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(..., gt=0),
        q: str = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


"""
{
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
}
=======  embed=True
{
  "item": {
    "name": "string",
    "description": "string",
    "price": 0,
    "tax": 0
  }
}
"""


@app.put("/items3/{item_id}")
async def update_item3(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
