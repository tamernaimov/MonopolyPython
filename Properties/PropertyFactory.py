from Properties.Land import Land

#price, level, owner, county(for monopoly),

class PropertyFactory():
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        self.name = name
        self.rent = rent
        self.price = price
        self.level = level
        self.country = country
        self.typeOfBuilding = typeOfBuilding
        self.is_owned = False

    def createB(self):
        if self.typeOfBuilding == "Land":
            return Land(self.name,self.price,self.rent,self.level,self.country,self.typeOfBuilding)