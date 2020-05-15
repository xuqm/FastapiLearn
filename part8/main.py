from typing import List, Set, Dict

from pydantic import BaseModel, HttpUrl

from part8 import app


# https://fastapi.tiangolo.com/tutorial/body-nested-models/

@app.get("/")
async def root():
    return {"message": "Hello World"}


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    tags1: list = []
    tags2: List[Image] = []
    tags3: Set[str] = []
    image: Image = None


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results


@app.post("/images/multiple/")
async def create_multiple_images(*, images: List[Image]):
    return images


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[str, str]):
    return weights
