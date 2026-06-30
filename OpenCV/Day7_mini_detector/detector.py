import cv2
import preprocessing
import contour
import scoring
import nms
import config as cfg
import visualizer


def detect(img):

    images = {}

    # =====================
    # original
    # =====================
    images["original"] = img.copy()

    # =====================
    # preprocess
    # =====================
    _, _, edges = preprocessing.preprocess(img)

    # images["gray"] = gray
    # images["blur"] = blur
    images["edges"] = edges

    # =====================
    # contours stage
    # =====================
    binary = edges.copy()
    contours, _ = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contour_vis = img.copy()

    boxes = []

    for c in contours:

        x, y, w, h = cv2.boundingRect(c)

        area = w * h
        if area < cfg.MIN_AREA:
            continue

        aspect = w / float(h)
        if aspect < cfg.ASPECT_MIN or aspect > cfg.ASPECT_MAX:
            continue

        boxes.append((x, y, w, h))

        cv2.rectangle(contour_vis,
                      (x, y),
                      (x+w, y+h),
                      (255, 0, 0), 2)

    images["contours"] = contour_vis

    # =====================
    # scoring
    # =====================
    scores = scoring.score_boxes(boxes)

    # =====================
    # NMS
    # =====================
    keep = nms.nms(boxes, scores, cfg.NMS_IOU_THRESH)

    final_boxes = [boxes[i] for i in keep]
    final_scores = [scores[i] for i in keep]

    # =====================
    # final
    # =====================
    final_img = visualizer.draw_boxes(
        img.copy(),
        final_boxes,
        final_scores
    )

    images["final"] = final_img

    return final_boxes, final_scores, images