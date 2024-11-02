from Player import Player
from Properties.Property import Property

class MakeMonopoly():
    def __init__(self):
        self.properties = []

    def fromSpaceToProperties(self,space):
        self.countries = []
        self.propertiesFromCountry = []

        for space in space: #add all the properties in
            if isinstance(space, Property):
                self.properties.append(space)

        for property in self.properties:
            self.countries.append(property.country) #add countries

        self.countries = list(set(self.countries)) #remove duplicates

        #for country in self.countries:
            #for user in self.users:


        #for country in self.countries:
            #print(country)
