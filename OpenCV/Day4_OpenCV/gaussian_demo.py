import cv2

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# 高斯滤波
blur = cv2.GaussianBlur(
    gray,
    (5,5),
    0
)

edges = cv2.Canny(
    blur,
    100,
    200
)

cv2.imwrite(
    "images/gaussian_edges.jpg",
    edges
)

print("Done")