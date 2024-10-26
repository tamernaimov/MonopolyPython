from abc import ABC, abstractmethod
#price, level, owner, county(for monopoly),

class Property(ABC):
    def __init__(self,price,rent,level,country,owner):
        self.rent = rent
        self.price = price
        self.level = level
        self.country = country
        self.owner = owner

    @abstractmethod
    def action(self):
        pass