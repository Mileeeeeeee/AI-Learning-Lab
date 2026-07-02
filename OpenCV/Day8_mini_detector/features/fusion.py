from .color import ColorFeature
from .texture import TextureFeature
from .edge import EdgeFeature


class FeatureFusion:

    def __init__(self):

        self.color = ColorFeature()
        self.texture = TextureFeature()
        self.edge = EdgeFeature()

    def extract(self, image, box):

        return {

            "color": self.color.extract(image, box),

            "texture": self.texture.extract(image, box),

            "edge": self.edge.extract(image, box)

        }