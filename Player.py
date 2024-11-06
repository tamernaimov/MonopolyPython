#value = input("Some String")
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # Import Property only for type checking, which prevents circular imports at runtime
    from Properties.Property import Property

class Player():

    players = []
    def __init__(self,name):
        self.name = name
        self.money = 1000000  # Starting money
        self.position = 0  # Initial position
        self.ownedProperty: list[Property] = []
        self.ownedPropertyCountries = []
        self.ownedBeaches = []
        self.inJail = False
        self.hasJailCard = False
        self.travelling = False