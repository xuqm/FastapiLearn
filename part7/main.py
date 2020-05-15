from fastapi import Body
from pydantic import BaseModel, Field

from part7 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Field model的验证  类比 path query body
class Item(BaseModel):
    name: str
    description: str = Field(None, title="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: float = None


@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
