import os

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, File, UploadFile, Depends
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.templating import Jinja2Templates

from evacuate_us.container import Container
from evacuate_us.services.give_map import upload_image_get_dest

exit_router = APIRouter()


@exit_router.post("/exit")
@inject
async def exit_give_map(request: Request,
                        templates: Jinja2Templates = Depends(Provide[Container.templates]),
                        file: UploadFile = File()):
    dest, width, height = upload_image_get_dest(file)
    return templates.TemplateResponse("image.html",
                                      context={"request": request,
                                               "path": f"/img/{os.path.basename(dest + '.svg')}",
                                               "width": width,
                                               "height": height})


@exit_router.get('/exit/coords')
@inject
async def after_get_coords(request: Request,
                           x, y,
                           templates: Jinja2Templates = Depends(Provide[Container.templates])):
    return JSONResponse({})
