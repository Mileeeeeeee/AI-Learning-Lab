import cv2
import numpy as np

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

kernel = np.ones((3,3), np.uint8)

opening = cv2.morphologyEx(
    binary,
    cv2.MORPH_OPEN,
    kernel
)

cv2.imwrite(
    "results/opening.jpg",
    opening
)

print("Opening completed.")