from Properties.Property import Property
class Hotel():
#price, level, owner, county(for monopoly),
    def __init__(self,name,price,rent,level,country):
        super().__init__(name,price,rent,level,country)
        self.owner = ""
        self.is_owned = False



    def action(self,player):
        print("ACTION HAPPENED!")