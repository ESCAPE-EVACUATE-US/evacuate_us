import cv2
import numpy as np
from matplotlib import image


def image_to_array(path):
    open_cv_image = cv2.imread(path)
    shape = open_cv_image.shape
    arr = np.full(shape=shape[:-1], fill_value=0.)

    for i in range(shape[0]):
        for j in range(shape[1]):
            tmp = open_cv_image[i][j]
            if tmp[0] < 95 and tmp[1] < 20 and tmp[2] < 95:
                arr[i][j] = 1
                open_cv_image[i][j] = [0., 0., 0.]
            else:
                open_cv_image[i][j] = [255., 255., 255.]

    return arr.tolist(), open_cv_image
