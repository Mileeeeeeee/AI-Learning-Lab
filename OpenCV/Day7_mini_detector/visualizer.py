import cv2
import math


def draw_boxes(img, boxes, scores=None):

    for i, (x, y, w, h) in enumerate(boxes):

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if scores is not None:
            cv2.putText(img,
                        f"{scores[i]:.2f}",
                        (x, y-5),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 255, 0), 1)

    return img

import cv2
import math
import numpy as np


def to_bgr(img):
    """
    保证所有图都是 3 通道
    """
    if len(img.shape) == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return img


def auto_montage(images, max_width=1200):

    # =====================
    # 1. 统一 BGR
    # =====================
    images = [to_bgr(img) for img in images]

    n = len(images)
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n / cols)

    h, w = images[0].shape[:2]

    scale = min(max_width / (cols * w), 1.0)

    resized = [
        cv2.resize(img, (int(w * scale), int(h * scale)))
        for img in images
    ]

    # =====================
    # 2. 补空白图
    # =====================
    blank = np.zeros_like(resized[0])

    while len(resized) < rows * cols:
        resized.append(blank)

    # =====================
    # 3. 拼接 rows
    # =====================
    row_imgs = []

    for i in range(rows):
        row = resized[i*cols:(i+1)*cols]

        # 再保险：保证每行一致
        row_imgs.append(cv2.hconcat(row))

    # =====================
    # 4. 最终拼接
    # =====================
    return cv2.vconcat(row_imgs)