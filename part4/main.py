from typing import List

from fastapi import Query

from part4 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Query 第一个参数是默认值，None表示可空   ...表示必需
@app.get("/items1/")
async def read_items1(q: str = Query(..., min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 查询参数可以是列表，表示参数可以出现多次
# /items2/?q=ewq&q=rwqe&q=rt
# 需要显示的使用  Query   否则会解析为body
@app.get("/items2/")
async def read_items2(q: List[str] = Query(None)):
    query_items = {"q": q}
    return query_items


@app.get("/items3/")
async def read_items3(
        q: str = Query(
            None,
            title="Hello World",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# alias 定义一个别名，
# /items4/?item-query=dsa
@app.get("/items4/")
async def read_items4(q: str = Query(None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


""""
deprecated=True
表示弃用参数
"""
