import cv2
from detector import detect
from visualizer import auto_montage
from utils import save_image, save_montage
import config as cfg


def run():

    img = cv2.imread(cfg.IMAGE_PATH)

    if img is None:
        print("[ERROR] image not found")
        return

    boxes, scores, images = detect(img)

    # =====================
    # 1. montage
    # =====================
    montage = auto_montage(list(images.values()))

    # =====================
    # 2. 保存 montage（关键恢复点）
    # =====================
    save_montage(montage, "pipeline.jpg")

    # =====================
    # 3. 保存 final detection
    # =====================
    save_image(images["final"], "final.jpg")


if __name__ == "__main__":
    run()