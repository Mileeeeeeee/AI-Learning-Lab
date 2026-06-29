import cv2
import numpy as np
import json


def score(c):
    area = cv2.contourArea(c)

    if area < 500:
        return 0

    x, y, w, h = cv2.boundingRect(c)
    aspect = w / float(h)

    s = area / 1000

    if 0.6 < aspect < 2.2:
        s += 5
    else:
        s -= 2

    return s



img = cv2.imread("images/test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)

_, binary = cv2.threshold(
    blur, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

kernel = np.ones((3,3), np.uint8)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

detections = []

for c in contours:
    s = score(c)

    if s < 3:
        continue

    x, y, w, h = cv2.boundingRect(c)

    detections.append({
        "score": float(s),
        "bbox": [int(x), int(y), int(w), int(h)]
    })


detections = sorted(detections, key=lambda x: x["score"], reverse=True)

result = img.copy()

for i, det in enumerate(detections):
    x, y, w, h = det["bbox"]
    s = det["score"]

    cv2.rectangle(result, (x,y), (x+w,y+h), (0,255,0), 2)

    cv2.putText(
        result,
        f"Obj{i} {s:.1f}",
        (x, y-5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0,255,0),
        1
    )


best = detections[0] if detections else None

if best:
    x, y, w, h = best["bbox"]

    cv2.rectangle(result, (x,y), (x+w,y+h), (0,0,255), 3)
    cv2.putText(result, "BEST", (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0,0,255), 2)
    

with open("detections.json", "w") as f:
    json.dump(detections, f, indent=4)

cv2.imwrite("result/result_yolo.jpg", result)

print("Saved: result_yolo.jpg + detections.json")