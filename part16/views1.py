# coding=utf-8
"""
@author: xuqm
@contact: xuqinmin12@sina.com
@file: views1.py
@time: 2020/7/1 下午 2:07
@desc:
"""
from part16.routers import router


@router.get("/", tags=["111"])
async def root():
    return {"message": "Hello World"}
