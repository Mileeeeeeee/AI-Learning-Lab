import cv2
import numpy as np


img = cv2.imread("images/test.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5,5), 0)

_, binary = cv2.threshold(blur, 0, 255,
                          cv2.THRESH_BINARY + cv2.THRESH_OTSU)

kernel = np.ones((3,3), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=1)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel, iterations=2)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

filtered = [c for c in contours if cv2.contourArea(c) > 1000]

filtered = sorted(filtered, key=cv2.contourArea, reverse=True)

result = img.copy()

for c in filtered:
    cv2.drawContours(result, [c], -1, (0,0,255), 2)

print("Final contours:", len(filtered))

cv2.imwrite("result/result.jpg", result)