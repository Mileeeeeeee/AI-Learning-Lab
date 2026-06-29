import cv2

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

print(gray.shape)

cv2.imwrite(
    "images/gray.jpg",
    gray
)