from fastapi import FastAPI

from part16 import routers


def create_app():
    app = FastAPI(title="路由练习")
    app.include_router(routers.router)
    return app
