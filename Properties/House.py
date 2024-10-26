from Properties.Property import Property
class House(Property):
#price, level, owner, county(for monopoly),
    def __init__(self,price,rent,level,country,owner):
        super().__init__(price,rent,level,country,owner)


    def action(self):
        print("ACTION HAPPENED!")