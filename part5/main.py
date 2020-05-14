from fastapi import Query, Path

from part5 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Path  和query 相同？？？  ?后面的参数要用query验证，path上面的参数要用path验证
# path  默认值是必须的 (第一个参数设置成 None 或者 默认值 都没有效果 因为path必须要有一个数值)
# 比如  默认值设置为5  docs 尝试item_id不传值也是不可以的
@app.get("/items1/{item_id}")
async def read_items1(
        item_id: int = Path(..., title="The ID of the item to get"),
        q: str = Query(None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 第一个参数是   *    表示后面的参数都是关键字参数(键值对),哪怕它们是没有默认值的
@app.get("/items2/{item_id}")
async def read_items2(
        *, item_id: int = Path(..., title="The ID of the item to get"), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# ge 表示大于等于
# gt 表示大于
# le 小于等于 ？
# lt 小于 ？
@app.get("/items3/{item_id}")
async def read_items3(
        *, item_id: int = Path(..., title="The ID of the item to get", gt=5), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
