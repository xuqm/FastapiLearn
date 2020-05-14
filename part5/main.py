
from fastapi import Query, Path

from part5 import app


@app.get("/")
async def root():
    return {"message": "Hello World"}

