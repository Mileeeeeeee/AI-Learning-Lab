import cv2
import os
import config as cfg


def save_image(img, name="result.jpg"):
    """
    保存单张图片
    """
    path = os.path.join(cfg.OUTPUT_DIR, name)
    cv2.imwrite(path, img)
    print(f"[SAVE] {path}")


def save_montage(img, name="montage.jpg"):
    """
    保存拼接结果
    """
    path = os.path.join(cfg.OUTPUT_DIR, name)
    cv2.imwrite(path, img)
    print(f"[SAVE] {path}")