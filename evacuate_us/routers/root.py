from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from evacuate_us.container import Container
from evacuate_us.database import Database

root_router = APIRouter()


@root_router.get('/', response_class=HTMLResponse)
@inject
async def root(request: Request,
               db: Database = Depends(Provide[Container.db]),
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("index.html", context={"request": request})
