import cv2
import config as cfg

def get_boxes(binary_img):

    contours, _ = cv2.findContours(
        binary_img,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    boxes = []

    for c in contours:

        x, y, w, h = cv2.boundingRect(c)

        area = w * h
        if area < cfg.MIN_AREA:
            continue

        aspect = w / float(h)
        if aspect < cfg.ASPECT_MIN or aspect > cfg.ASPECT_MAX:
            continue

        boxes.append((x, y, w, h))

    return boxes