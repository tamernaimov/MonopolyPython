from abc import ABC, abstractmethod

class Card(ABC):
    @abstractmethod
    def showCard(self):
        pass