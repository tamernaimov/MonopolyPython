from typing import List
from Properties.Property import Property

class MakeMonopoly():
    def __init__(self):
        self.properties: List[Property] = [] #removed '' (could be a problem)
        self.countries = []
        self.countriesWithMonopoly = []

    def fromSpaceToProperties(self,space,player):
        if len(self.countries) == 0:
            for space in space: #add all the properties in
                if isinstance(space, Property):
                    self.properties.append(space)

            for prop in self.properties:
                self.countries.append(prop.country) #add countries

        countriesSorted = list(dict.fromkeys(self.countries)) #remove duplicates

        for countrySorted in countriesSorted: #for every country (no dupes)
            counter1 = 0
            counter2 = 0
            for owned in player.ownedProperty: #for each owned country
                if owned.country == countrySorted:
                    counter1 +=1 #how many properties from spain (for example)

            for country in self.countries:
                if country == countrySorted:
                    counter2 += 1

            if counter1 == counter2: #and counter2 != 0
                print(f"WOW YOU GOT A MONOPOLY IN {countrySorted}!!!")
                self.countriesWithMonopoly.append(countrySorted)
                self.countriesWithMonopoly= list(dict.fromkeys(self.countriesWithMonopoly)) #remove dupes
                self.updateProperty()

    def updateProperty(self):
        for prop in self.properties:
            if prop.country == self.countriesWithMonopoly and prop.inMonopoly == False:
                prop.price = prop.price * 2
                prop.rent = prop.rent * 2
                prop.inMonopoly = True
                print(f"The Property {prop.name} Has Just Been Upgraded(Doubled - Price and Rent) Due to Monopoly!")