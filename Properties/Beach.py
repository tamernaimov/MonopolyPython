from Properties.Property import Property


class Beach():
    def __init__(self,price,rent,owner):
        self.price = price
        self.rent = rent
        self.owner = owner


    def action(self,player):
        print("ACTION HAPPENED!")