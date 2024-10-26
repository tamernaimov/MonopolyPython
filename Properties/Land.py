from Properties.Property import Property
class Land(Property):

    def __init__(self,price,rent,level,country,is_owned):
        self.price = price
        self.rent = rent
        self.level = level
        self.country = country
        self.is_owner = is_owned
        self.land = []


    def action(self):
        print("ACTION HAPPENED!")