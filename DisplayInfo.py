from Properties.Property import Property


class DisplayInfo():
    def __init__(self):
        self.properties = []
        self.countries = []

    def displayInfo(self, player, space):

        if len(self.countries) == 0:
            for space in space:
                if isinstance(space, Property):
                    self.properties.append(space)

            for property in self.properties:
                self.countries.append(property.country)  # add countries

        countriesSorted = list(dict.fromkeys(self.countries))  # remove duplicates

        seperator = ", "
        print("\nOwned Properties:")
        if not player.ownedProperty:
            print("You Do not have any properties")
        for country in countriesSorted:
            property_names = []
            for prop in player.ownedProperty:
                if prop.country == country:
                    property_names.append(prop.name)

            if property_names:  # Check if there are any properties for this country
                formatted_properties = seperator.join(property_names)
                print(f"{country}: {formatted_properties}")

        print(f"\n{player.name}'s Current balance - {player.money}\n \n ---------------NEXT TURN--------------- \n")

