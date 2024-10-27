
from Properties.House import House
from Properties.Property import Property
class Land(Property):
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        super().__init__(name,price,rent,level,country,typeOfBuilding)
        self.owner = ""
        self.is_owned = False
        #self.land = []


    def action(self, player):
        if self.is_owned == False:
            if self.level == 0:
                answer = input("this is not bought! Would you like to buy it?")
                if answer == "y":
                    #change it with another function
                    player.money -= self.price #remove the money
                    player.ownedProperty.append(self) #add the land to the player's owned property
                    self.owner = player.name #this is the owner of the property after being bought
                    self.is_owned = True
                    print(f"You've bought {self.name}")

        elif self.is_owned == True and player.name != self.owner:
            print(f"You've landed on {self.owner}'s property! You pay {self.rent}$ then!")
            player.money -= self.rent

        elif self.is_owned == True and player.name == self.owner:
            buyOrNot = input(f"You are on your own property!: {self.name}, Would you like to upgrade it(get it to the next level)?")
            if buyOrNot.lower() == "y":
                return House(self.name,self.price,self.rent,self.level,self.country,"House")
        return None

