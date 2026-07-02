from features.color import ColorFeature


class Scoring:

    def __init__(self):

        self.color_feature = ColorFeature()

    def score(self, image, boxes):

        scores = []

        for box in boxes:

            s = self.color_feature.extract(image, box)

            scores.append(s)

        return scores