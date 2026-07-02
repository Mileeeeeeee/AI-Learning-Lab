from abc import ABC, abstractmethod


class FeatureExtractor(ABC):

    @abstractmethod
    def extract(self, image, box):
        """返回一个特征值或特征向量"""
        pass