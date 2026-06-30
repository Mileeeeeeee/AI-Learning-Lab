# iou.py

def iou(box1, box2):
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2

    xa = max(x1, x2)
    ya = max(y1, y2)
    xb = min(x1 + w1, x2 + w2)
    yb = min(y1 + h1, y2 + h2)

    inter_w = max(0, xb - xa)
    inter_h = max(0, yb - ya)

    inter = inter_w * inter_h

    area1 = w1 * h1
    area2 = w2 * h2

    union = area1 + area2 - inter

    return inter / union if union > 0 else 0