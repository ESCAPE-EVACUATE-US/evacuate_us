from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from evacuate_us.container import Container
from evacuate_us.routers.root import root_router
from evacuate_us.routers.alert import alert_router


def create_app() -> FastAPI:
    container = Container()

    app = FastAPI()
    app.mount("/static", StaticFiles(directory="evacuate_us/static"), name="static")
    app.container = container
    app.include_router(root_router)
    app.include_router(alert_router)
    return app


app = create_app()
