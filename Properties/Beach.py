from Properties.Property import Property


class Beach(Property):
    def __init__(self,price,rent,owner):
        self.price = price
        self.rent = rent
        self.owner = owner


    def action(self):
        print("ACTION HAPPENED!")