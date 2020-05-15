from pydantic import BaseModel, EmailStr

from part13 import app


# https://fastapi.tiangolo.com/tutorial/extra-models/

@app.get("/")
async def root():
    return {"message": "Hello World"}


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str = None


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
    print(user_saved)
    return user_saved
