from .base import ProposalGenerator
import config as cfg


class GridProposal(ProposalGenerator):

    def __init__(self, step):
        self.step = step

    def generate(self, image):

        h, w = image.shape[:2]

        proposals = []

        for y in range(0, h, self.step):
            for x in range(0, w, self.step):

                bw = min(self.step, w - x)
                bh = min(self.step, h - y)

                proposals.append((x, y, bw, bh))

        return proposals