import cv2
import numpy as np


class TextureFeature:

    def extract(self, image, box):

        x, y, w, h = box

        patch = image[y:y+h, x:x+w]

        if patch.size == 0:
            return 0.0

        gray = cv2.cvtColor(patch, cv2.COLOR_BGR2GRAY)

        gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0)
        gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1)

        magnitude = np.sqrt(gx**2 + gy**2)

        return float(np.mean(magnitude))