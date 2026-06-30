import config as cfg

def score_box(box):
    x, y, w, h = box

    area = w * h
    score = area / cfg.SCORE_AREA_DIV

    aspect = w / float(h)

    if 0.5 < aspect < 2.5:
        score += 5

    return score


def score_boxes(boxes):
    return [score_box(b) for b in boxes]