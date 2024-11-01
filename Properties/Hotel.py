from Properties.Property import Property
from Space import Space


class Hotel(Space,Property):
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,country,typeOfBuilding):
        super().__init__(name,price,rent,country,typeOfBuilding)
        self.level = 5


    def action(self,player):
        print("ACTION HAPPENED!")