from typing import List

from fastapi import Cookie, Header

from part11 import app


# https://fastapi.tiangolo.com/tutorial/cookie-params/

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/cookie/")
async def read_items1(*, ads_id: str = Cookie(None)):
    return {"ads_id": ads_id}


@app.get("/items/header/")
async def read_items2(*, user_agent: str = Header(None)):
    return {"User-Agent": user_agent}


# convert_underscores=True   使得  strange_header  ==》 strange-header
@app.get("/items1/")
async def read_items1(*, strange_header: str = Header(None, convert_underscores=True)):
    return {"strange_header": strange_header}


# 传多个token  -H "x-token: dsad,sfad,grew"
@app.get("/items2/")
async def read_items2(x_token: List[str] = Header(None)):
    return {"X-Token values": x_token}
