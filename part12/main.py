from typing import List

from pydantic import BaseModel, EmailStr

from part12 import app


# https://fastapi.tiangolo.com/tutorial/cookie-params/

@app.get("/")
async def root():
    return {"message": "Hello World"}


# response_model  定义输出模型
class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


# Don't do this in production!
@app.post("/user1/", response_model=UserIn)
async def create_user1(*, user: UserIn):
    return user


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


# 输入包含password   输出不包含
@app.post("/user2/", response_model=UserOut)
async def create_user2(*, user: UserIn):
    return user


class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# response_model_exclude_unset  忽略有默认值的参数
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
