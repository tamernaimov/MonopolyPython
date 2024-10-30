from Properties.Property import Property
from Space import Space


class Beach(Space):
    def __init__(self,name,price,rent):
        self.price = price
        self.rent = rent
        self.owner = ""

    def action(self,player):
        print("BEACH ACTION HAPPENED!")