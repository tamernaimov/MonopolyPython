from Properties.Land import Land

class PropertyFactory():
    def __init__(self,name,price,rent,country,typeOfBuilding):
        self.name = name
        self.rent = rent
        self.price = price
        self.country = country
        self.typeOfBuilding = typeOfBuilding
        self.is_owned = False

    def createB(self):
        if self.typeOfBuilding == "Land":
            return Land(self.name,self.price,self.rent,self.country,self.typeOfBuilding)