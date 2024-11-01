import contextlib
import io

from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Property import Property
from Space import Space

class Land(Space,Property):
    def __init__(self,name,price,rent,country,typeOfBuilding):
        super().__init__(name,price,rent,country,typeOfBuilding)

    def buyProperty(self,player):
        if self.is_owned == False and self.level == 0:
            answer = input(f"this property is not bought! Would you like to buy {self.name}?: ")
            if answer == "y":
              super().updateProperty(player) #level should be 1
            if answer == "n":
                print("Okay, you won't get it then!")

    def defineType(self):
        result = super().define()
        if result == "Land":
           return self
        elif result == "House":
            house = House(self.name, self.price * 2, self.rent * 2, self.country, "House")
            return house


    def action(self, player):
        self.buyProperty(player) #buying property from self because it is Land
        super().payRent(player) #check for rent through Property
        super().tradeProperty(player) #check for trading
        super().upgrade(player) #check for upgrading
        result = self.defineType() #defines the type of Property --> returns the property

        self.justBought = False # needed for the
        return result
