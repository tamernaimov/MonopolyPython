import contextlib
import io

from Player import Player
from Properties.Hotel import Hotel
from Properties.House import House
from Properties.Property import Property
from Space import Space

class Land(Space,Property):
    def __init__(self,name,price,rent,country,typeOfBuilding):
        super().__init__(name,price,rent,country,typeOfBuilding)

    def buyProperty(self,player: Player):
        if self.is_owned == False and self.level == 0:
            answer = input(f"This Property Has Not Been Bought Yet! Would You Like to Buy {self.name}? y/n: ")
            if answer == "y" and player.money >= self.price:
              super().updateProperty(player) #level should be 1
            else:
                print("Your Loss!!")

    def defineType(self):
        result = super().define() #returns the property type by level
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

        self.justBought = False # needed for the upgrading part
        return result #returning the object (Could be land, could be house)
