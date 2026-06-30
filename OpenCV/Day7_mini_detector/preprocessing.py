import cv2
import config as cfg
import numpy as np


def preprocess(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (cfg.BLUR_K1, cfg.BLUR_K2), 0)

    edges = cv2.Canny(blur, cfg.CANNY_LOW, cfg.CANNY_HIGH)

    # 形态学闭运算（连碎片）
    kernel = np.ones((cfg.BLUR_K1, cfg.BLUR_K2), np.uint8)
    edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    return gray, blur, edges