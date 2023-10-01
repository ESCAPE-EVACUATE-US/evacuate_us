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
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("main_page.html", context={"request": request})


@root_router.get('/fire', response_class=HTMLResponse)
@inject
async def root(request: Request,
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("fire.html", context={"request": request})


@root_router.get('/gas', response_class=HTMLResponse)
@inject
async def root(request: Request,
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("gas.html", context={"request": request})


@root_router.get('/how_to_use', response_class=HTMLResponse)
@inject
async def root(request: Request,
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("how_to_use.html", context={"request": request})


@root_router.get('/model', response_class=HTMLResponse)
@inject
async def root(request: Request,
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("model.html", context={"request": request})


@root_router.get('/safe_rec', response_class=HTMLResponse)
@inject
async def root(request: Request,
               templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return templates.TemplateResponse("safe_rec.html", context={"request": request})
