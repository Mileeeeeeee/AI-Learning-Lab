import cv2
import numpy as np

# 读取图片
img = cv2.imread("images/test.jpg")

# 灰度
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 二值化
_, binary = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

# Kernel
kernel = np.ones((5,5), np.uint8)

# Closing
closing = cv2.morphologyEx(
    binary,
    cv2.MORPH_CLOSE,
    kernel
)

cv2.imwrite(
    "result/closing.jpg",
    closing
)

print("Closing Done")