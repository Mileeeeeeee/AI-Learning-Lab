from abc import ABC, abstractmethod


class ProposalGenerator(ABC):

    @abstractmethod
    def generate(self, image):
        """
        返回：
        List[(x,y,w,h)]
        """
        pass