import cv2
import numpy as np
from matplotlib import image


def image_to_array(path):
    open_cv_image = cv2.imread(path)
    shape = open_cv_image.shape

    img_out = np.full(shape=shape, fill_value=80.)
    arr = np.full(shape=shape[:-1], fill_value=0.)
    t = cv2.convertScaleAbs(open_cv_image, beta=-80)
    for i in range(shape[0]):
        for j in range(shape[1]):
            tmp = t[i][j]
            if 20 <= tmp[1] <= 120 and tmp[2] <= 84:
                img_out[i][j] = [0., 150., 0.]
    t = cv2.convertScaleAbs(open_cv_image, beta=-10)
    for i in range(shape[0]):
        for j in range(shape[1]):
            tmp = t[i][j]
            if tmp[0] < 100 and tmp[1] < 45 and tmp[2] < 60:
                arr[i][j] = 1
                img_out[i][j] = [0., 0., 0.]

    image.imsave("test.svg", format="svg", arr=img_out)

    return arr.tolist()
