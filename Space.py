from abc import ABC, abstractmethod
class Space(ABC):
    @abstractmethod
    def action(self, player):
        pass