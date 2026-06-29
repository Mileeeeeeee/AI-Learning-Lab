import cv2

img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

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

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

result = img.copy()

cv2.drawContours(
    result,
    contours,
    -1,
    (0,255,0),
    2
)

print("Contours:", len(contours))

cv2.imwrite(
    "images/contours.jpg",
    result
)

MIN_AREA = 100

filtered_contours = []

for cnt in contours:

    area = cv2.contourArea(cnt)

    if area > MIN_AREA:
        filtered_contours.append(cnt)

print("Before:", len(contours))
print("After:", len(filtered_contours))

result = img.copy()
cv2.drawContours(
    result,
    filtered_contours,
    -1,
    (0,255,0),
    2
)

cv2.imwrite(
    "images/contours_MIN_AREA-" + str(MIN_AREA) + ".jpg",
    result
)