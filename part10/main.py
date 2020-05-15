from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import Body

from part10 import app


# https://fastapi.tiangolo.com/tutorial/extra-data-types/

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: datetime = Body(None),
        end_datetime: datetime = Body(None),
        repeat_at: time = Body(None),
        process_after: timedelta = Body(None),
):
    start_process = start_datetime + process_after  # 常规的日期操作
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


"""
UUID：
一个标准的“通用唯一标识符”，在许多数据库和系统中通常作为ID使用。
在请求和响应中将以表示str。
datetime.datetime：
一个Python datetime.datetime。
在请求和响应中，将以strISO 8601格式表示，例如：2008-09-15T15:53:00+05:00。
datetime.date：
Python datetime.date。
在请求和响应中，将以strISO 8601格式表示，例如：2008-09-15。
datetime.time：
一个Python datetime.time。
在请求和响应中，将以strISO 8601格式表示，例如：14:23:55.003。
datetime.timedelta：
一个Python datetime.timedelta。
在请求和响应中，将以float总秒数表示。
Pydantic还允许将其表示为“ ISO 8601时间差异编码”，有关更多信息，请参阅文档。
frozenset：
在请求和响应中，将与视为相同set：
在请求中，将读取列表，消除重复，并将其转换为set。
作为响应，set将会转换为list。
生成的架构将指定set值是唯一的（使用JSON架构的uniqueItems）。
bytes：
标准Python bytes。
在请求和响应中将被视为str。
生成的模式将指定，这是一个str与binary“格式”。
Decimal：
标准Python Decimal。
在请求和响应中，处理方式与相同float。
"""
