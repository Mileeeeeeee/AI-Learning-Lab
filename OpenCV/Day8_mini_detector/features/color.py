import cv2
import numpy as np


class ColorFeature:

    def extract(self, image, box):
        """
        box: (x, y, w, h)
        """

        x, y, w, h = box

        patch = image[y:y+h, x:x+w]

        if patch.size == 0:
            return 0

        # 转 HSV（更稳定）
        hsv = cv2.cvtColor(patch, cv2.COLOR_BGR2HSV)

        # 计算方差
        std = np.std(hsv, axis=(0, 1))

        score = 1.0 / (np.mean(std) + 1e-6)

        return float(score)