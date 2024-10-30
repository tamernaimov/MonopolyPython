from Space import Space


class House(Space):
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,level,country,typeOfBuilding):
        self.name = name
        self.price = price
        self.rent = rent
        self.level = level
        self.country = country
        self.typeOfBuilding = typeOfBuilding
        self.owner = ""
        self.is_owned = False



    def action(self,player):
        print("ACTION HAPPENED!")