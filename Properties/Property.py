from abc import ABC, abstractmethod
#price, level, owner, county(for monopoly),

class Property(ABC):
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        self.name = name
        self.rent = rent
        self.price = price
        self.level = level
        self.country = country
        self.typeOfBuilding = typeOfBuilding
        self.is_owned = False

    @abstractmethod
    def action(self,player):
        self.action(player)