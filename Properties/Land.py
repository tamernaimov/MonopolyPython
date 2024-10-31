import contextlib
import io

from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Property import Property
from Space import Space

class Land(Space,Property):
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        super().__init__(name,price,rent,level,country,typeOfBuilding)


    def updateProperty(self,player):
        player.money -= self.price
        player.ownedProperty.append(self)
        self.owner = player.name
        self.price = self.price * 2
        self.rent = self.rent *2
        self.level = self.level + 1
        self.is_owned = True

        print(f"You've bought {self.name}")

    def buyProperty(self,player):
        if self.is_owned == False and self.level == 0:
            answer = input(f"this property is not bought! Would you like to buy {self.name}?: ")
            if answer == "y":
              self.justBought = True
              self.updateProperty(player) #level should be 1
            if answer == "n":
                print("Okay, you won't get it then!")

    def defineType(self,player):
        result = super().upgrade(player)
        print(result)
        if result == "Land":
           return self
        elif result == "House":
            house = House(self.name, self.price * 2, self.rent * 2, self.level, self.country, "House")
            return house


    def action(self, player):
        self.buyProperty(player)
        super().payRent(player)
        result = self.defineType(player) #call the function for upgrading too


        self.justBought = False
        return result
