from Properties.Property import Property
from Space import Space


class Hotel(Space,Property):
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        super().__init__(name,price,rent,level,country,typeOfBuilding)



    def action(self,player):
        print("ACTION HAPPENED!")