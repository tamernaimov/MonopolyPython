from Space import Space


class Beach(Space):
    def __init__(self,name,price,rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = ""
        self.is_owned = False

    def updateBeach(self,player):
        self.owner = player.name
        self.is_owned = True
        player.ownedBeaches.append(self)

    def buyBeach(self,player):
        if self.is_owned == False:
            answer = input(f"this beach is not bought! Would you like to buy {self.name}?: ")
            if answer == "y":
                self.updateBeach(player)
            if answer == "n":
                print("Okay, you won't get it then!")

    def payRent(self, player):
        if self.is_owned == True and player.name != self.owner:
            print(f"You've landed on {self.owner}'s property! - {self.name} You pay {self.rent}$ then!")
            player.money -= self.rent


    def action(self,player):
        self.buyBeach(player)