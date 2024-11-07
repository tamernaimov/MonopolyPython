from Properties.Hotel import Hotel
from Properties.Property import Property
from Space import Space

class House(Space,Property):
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,country,typeOfBuilding):
        super().__init__(name,price,rent,country,typeOfBuilding)
        self.level = 2

    def defineType(self):
        result = super().define() #returns the property type by level
        if result == "Land":
            return self
        elif result == "House":
            house = House(self.name, self.price * 2, self.rent * 2, self.country, "House")
            return house
        elif result == "Hotel":
            hotel = Hotel(self.name, self.price*2, self.rent*2,self.country,"Hotel")
            return hotel

    def action(self, player):
        super().payRent(player)  # check for rent through Property
        super().tradeProperty(player)  # check for trading
        super().upgrade(player)  # check for upgrading
        result = self.defineType()  # defines the type of Property --> returns the property

        self.justBought = False  # needed for the upgrading part
        return result  # returning the object (Could be land, could be house)