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

kernel = np.ones((5,5), np.uint8)

dilation = cv2.dilate(
    binary,
    kernel,
    iterations=1
)

cv2.imwrite(
    "results/dilation.jpg",
    dilation
)

print("Dilation completed.")