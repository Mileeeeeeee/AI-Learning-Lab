import cv2

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

edges = cv2.Canny(
    gray,
    200,
    400
)

cv2.imwrite(
    "images/edge3.jpg",
    edges
)

print(edges.shape)