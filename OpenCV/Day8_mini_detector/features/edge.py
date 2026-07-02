import cv2
import numpy as np


class EdgeFeature:

    def extract(self, image, box):

        x, y, w, h = box

        patch = image[y:y+h, x:x+w]

        if patch.size == 0:
            return 0.0

        gray = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)

        edge = cv2.Canny(gray,80,160)

        return float(np.mean(edge > 0))