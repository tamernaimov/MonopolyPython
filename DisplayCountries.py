from Properties.Property import Property


class DisplayCountries():
    def __init__(self):
        self.properties = []
        self.countries = []
    def displayCountries(self, player, space):

        if len(self.countries) == 0:
            for space in space:
                if isinstance(space, Property):
                    self.properties.append(space)

            for property in self.properties:
                self.countries.append(property.country) #add countries

        countriesSorted = list(dict.fromkeys(self.countries))  # remove duplicates

        seperator = ", "
        print("\nOwned Properties:")
        for country in countriesSorted:
            property_names = []
            for prop in player.ownedProperty:
                if prop.country == country:
                    property_names.append(prop.name)

            if property_names:  # Check if there are any properties for this country
                formatted_properties = seperator.join(property_names)
                print(f"{country}: {formatted_properties}")