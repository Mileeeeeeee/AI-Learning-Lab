import cv2
import numpy as np

# 1. 读取图片
img = cv2.imread("images/test.jpg")

# 检查图片是否读取成功
if img is None:
    print("Error: 无法读取图片！")
    exit()

# 2. 转换为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Canny边缘检测
edges = cv2.Canny(gray, 100, 200)

# 4. 为了拼接，需要把灰度图和边缘图转换为3通道
gray_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# 5. 水平拼接
result = np.hstack([
    img,
    gray_bgr,
    edges_bgr
])

# 6. 保存结果
cv2.imwrite("images/result.jpg", result)

# 7. 输出信息
print("原图尺寸:", img.shape)
print("灰度图尺寸:", gray.shape)
print("边缘图尺寸:", edges.shape)
print("拼接图尺寸:", result.shape)

print("保存成功: images/result.jpg")