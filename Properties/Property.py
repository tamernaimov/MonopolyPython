from abc import ABC, abstractmethod
class Property(ABC):
    level = 0
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        self.name = name
        self.rent = rent
        self.price = price
        self.level = level
        self.country = country
        self.typeOfBuilding  = typeOfBuilding
        self.owner = ""
        self.justBought = False
        self.is_owned = False


    def define(self):
        if self.level == 0 or self.level == 1:
            return "Land"
        elif self.level == 2 or self.level == 3 or self.level == 4:
            return "House"
        elif self.level == 5:
            return "Hotel"

    def payRent(self,player):
        if self.is_owned == True and player.name != self.owner:
            print(f"You've landed on {self.owner}'s property! - {self.name} You pay {self.rent}$ then!")
            player.money -= self.rent


    def upgrade(self, player):
        if self.is_owned == True and player.name == self.owner and self.justBought == False:
            buyOrNot = input(
                f"You are on your own ({self.name}) property!: {self.name}, Would you like to upgrade it(get it to the next level)?: ")
            if buyOrNot.lower() == "y":# after that check for level and then define what string to return
                self.level = self.level + 1
                typeb = self.define()
                return typeb
            else:
                return None
