from iou import iou

def nms(boxes, scores, thresh=0.5):

    idxs = sorted(range(len(scores)),
                  key=lambda i: scores[i],
                  reverse=True)

    keep = []

    while idxs:
        current = idxs.pop(0)
        keep.append(current)

        idxs = [
            i for i in idxs
            if iou(boxes[current], boxes[i]) < thresh
        ]

    return keep