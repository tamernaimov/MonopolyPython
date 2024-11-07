from Properties.Property import Property
from Space import Space

class Hotel(Space,Property):
    def __init__(self,name,price,rent,country,typeOfBuilding):
        super().__init__(name,price,rent,country,typeOfBuilding)
        self.level = 5

    def defineType(self):
        result = super().define() #returns the property type by level
        if result == "Hotel":
            hotel = Hotel(self.name, self.price*2, self.rent*2,self.country,"Hotel")
            return hotel

    def action(self, player):
        super().payRent(player)  # check for rent through Property
        result = self.defineType()
        self.justBought = False  # needed for the upgrading part
        return result  # returning the object (Could be land, could be house)