import os
import shutil

from fastapi import UploadFile
from matplotlib import image

from evacuate_us.services.image_to_array import image_to_array


def upload_image_get_dest(file: UploadFile):
    upload_dir = os.path.join(os.getcwd(), "evacuate_us/static/img")

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    dest = os.path.join(upload_dir, file.filename)

    with open(dest, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    arr, img = image_to_array(dest)
    image.imsave(dest + ".svg", format="svg", arr=img)
    return dest
