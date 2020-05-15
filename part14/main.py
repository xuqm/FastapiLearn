from typing import Union

from pydantic import BaseModel, EmailStr

from part14 import app


# https://fastapi.tiangolo.com/tutorial/extra-models/    ---2

@app.get("/")
async def root():
    return {"message": "Hello World"}


# UserBase  可以少些一下重复代码
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(*, user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


class BaseItem(BaseModel):
    description: str
    type: str


class CarItem(BaseItem):
    type = "car"


class PlaneItem(BaseItem):
    type = "plane"
    size: int


items = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}


# Union 相应里面的 任何一种
@app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id: str):
    return items[item_id]
