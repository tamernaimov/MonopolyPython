from Properties.House import House
import contextlib
import io
from Space import Space

class Land(Space):
    def __init__(self,name,price,rent,level,country,typeOfBuilding):

        self.name = name
        self.price = price
        self.rent = rent
        self.level = level
        self.country = country
        self.typeOfBuilding = typeOfBuilding
        self.owner = ""
        self.is_owned = False
        self.justBought = False


    def updateProperty(self,player):
        player.money -= self.price
        player.ownedProperty.append(self)
        self.owner = player.name
        self.price = self.price * 2
        self.rent = self.rent * 2
        self.level = self.level + 1
        self.is_owned = True

        print(f"You've bought {self.name}")

    def buyProperty(self,player):
        if self.is_owned == False and self.level == 0:
            answer = input(f"this property is not bought! Would you like to buy {self.name}?: ")
            if answer == "y":
              self.justBought = True
              self.updateProperty(player)
            if answer == "n":
                print("Okay, you won't get it then!")


    def payRent(self,player):
        if self.is_owned == True and player.name != self.owner:
            print(f"You've landed on {self.owner}'s property! - {self.name} You pay {self.rent}$ then!")
            player.money -= self.rent


    def upgrade(self,player):
        if self.is_owned == True and player.name == self.owner and self.justBought == False:
            buyOrNot = input(f"You are on your own ({self.name}) property!: {self.name}, Would you like to upgrade it(get it to the next level)?: ")
            if buyOrNot.lower() == "y":
                house = House(self.name,self.price * 2,self.rent * 2,self.level,self.country,"House")
                return house
            else:
                return None

    def action(self, player):


        self.buyProperty(player)
        self.payRent(player)
        result = self.upgrade(player)
        if isinstance(result, House):
            return result
        self.justBought = False
        return None
