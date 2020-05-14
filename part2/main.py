from typing import Optional

from part2 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, ]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10, ):
    return fake_items_db[skip: skip + limit]


# 使用  Optional  说明limit可以为空
@app.get("/items/{item_id}")
async def read_user_item(item_id: str, limit: Optional[int] = None):
    item = {"item_id": item_id, "limit": limit}
    return item
