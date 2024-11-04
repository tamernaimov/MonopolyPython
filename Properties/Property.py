from abc import ABC, abstractmethod
from types import NoneType

from Player import Player


class Property(ABC):
    level = 0
    def __init__(self,name,price,rent,country,typeOfBuilding):
        self.name = name
        self.rent = rent
        self.price = price
        self.level = 0
        self.country = country
        self.typeOfBuilding  = typeOfBuilding
        self.owner = ""
        self.ownerOBJ:Player = None
        self.justBought = False
        self.is_owned = False
        self.inMonopoly = False

    def upgradeProperty(self):
        self.level = self.level + 1
        self.price = self.price + (self.price*1.5)

    def updateProperty(self,player):
        player.money -= self.price
        player.ownedProperty.append(self.name) #ONLY THE NAME
        player.ownedPropertyCountries.append(self.country)
        self.owner = player.name
        self.price = self.price * 2
        self.rent = self.rent *2
        self.level = self.level + 1
        self.ownerOBJ = player
        self.is_owned = True
        self.justBought = True

    def payRent(self,player):
        if self.is_owned == True and player.name != self.owner:
            print(f"You've landed on {self.owner}'s property! - {self.name} You pay {self.rent}$ then!")
            player.money -= self.rent


    def define(self):
        if self.level == 1:
            return "Land"
        elif self.level == 2 or self.level == 3 or self.level == 4:
            return "House"
        elif self.level == 5:
            return "Hotel"

    def upgrade(self, player):
        if self.is_owned == True and player.name == self.owner and self.justBought == False:
            buyOrNot = input(
                f"You are on your own ({self.name}) property!: {self.name}, Would you like to upgrade it(get it to the next level)?: ")
            if buyOrNot.lower() == "y" and player.money >= self.price:# after that check for level and then define what string to return
                self.upgradeProperty()
                print("You've successfully upgraded the property")
            else:
                print("You get NOTHING!")

    def tradeProperty(self,player):
        if self.is_owned == True and player.name != self.owner:
            answer = input(f"Would you like to buy this property from: {self.owner}?: ")
            if answer == "y" and player.money >= self.price:
                player.ownedProperty.append(self.name)
                player.ownedPropertyCountries.append(self.country)
                self.owner = player.name
                self.ownerOBJ.ownedProperty.remove(self.name) #potentional error here (debug it)
                self.ownerOBJ = player
                self.justBought = True
                player.money -= self.price
                print(f"This property now belongs to {player.name}")

            elif answer == "n":
                print("Well, you're not getting it then!")