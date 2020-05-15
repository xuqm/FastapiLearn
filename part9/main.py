from fastapi import Body
from pydantic import BaseModel, Field

from part9 import app


# https://fastapi.tiangolo.com/tutorial/schema-extra-example/

@app.get("/")
async def root():
    return {"message": "Hello World"}


# Config  配置doc 可以展示的默认值
class Item1(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

    class Config:
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


@app.put("/items1/{item_id}")
async def update_item1(*, item_id: int, item: Item1):
    results = {"item_id": item_id, "item": item}
    return results


# 可以直接使用example 配置
class Item2(BaseModel):
    name: str = Field(..., example="Foo")
    description: str = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: float = Field(None, example=3.2)


@app.put("/items2/{item_id}")
async def update_item2(*, item_id: int, item: Item2):
    results = {"item_id": item_id, "item": item}
    return results


class Item3(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None


@app.put("/items3/{item_id}")
async def update_item3(
        *,
        item_id: int,
        item: Item3 = Body(
            ...,
            example={
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            },
        )
):
    results = {"item_id": item_id, "item": item}
    return results
