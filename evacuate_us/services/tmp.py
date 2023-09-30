import cv2
import numpy as np


def image_to_array(path):
    open_cv_image = cv2.imread(path)
    shape = open_cv_image.shape
    arr = np.full(shape=shape[:-1], fill_value=0.)

    for i in range(shape[0]):
        for j in range(shape[1]):
            if sum(open_cv_image[i][j]) <= 70:
                arr[i][j] = 1

    return arr.tolist()
