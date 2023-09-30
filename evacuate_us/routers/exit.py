import os
import shutil
from typing import Optional

from fastapi import APIRouter, File, UploadFile, Form
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

from evacuate_us.services.tmp import image_to_array

exit_router = APIRouter()


class MyForm(BaseModel):
    file: Optional[UploadFile]


@exit_router.post("/exit")
async def exit_give_map(request: Request,
                        file: UploadFile = File()):
    upload_dir = os.path.join(os.getcwd(), "evacuate_us/static/img")
    # Create the upload directory if it doesn't exist
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # get the destination path
    dest = os.path.join(upload_dir, file.filename)
    print(dest)

    # copy the file contents
    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    arr = image_to_array(dest)

    return JSONResponse(content=arr)