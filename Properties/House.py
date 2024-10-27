from Properties.Property import Property
class House(Property):
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        super().__init__(name,price,rent,level,country,typeOfBuilding)
        self.owner = ""
        self.is_owned = False



    def action(self,player):
        print("ACTION HAPPENED!")