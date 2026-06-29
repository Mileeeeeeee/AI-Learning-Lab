import cv2
import numpy as np

# 1. 读取图片
img = cv2.imread("images/test.jpg")

if img is None:
    raise FileNotFoundError("Cannot find images/test.jpg")

# 2. 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. 二值化
_, binary = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

# 4. 定义卷积核
kernel = np.ones((5, 5), np.uint8)

# 5. 腐蚀
erosion = cv2.erode(
    binary,
    kernel,
    iterations=1
)

# 6. 保存结果
cv2.imwrite("results/erosion.jpg", erosion)
cv2.imwrite("results/binary.jpg", binary)
print("Erosion completed.")
print("Kernel size:", kernel.shape)
