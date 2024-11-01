#value = input("Some String")
class Player():

    players = []
    def __init__(self,name):
        self.name = name
        self.money = 1000000  # Starting money
        self.position = 0  # Initial position
        self.ownedProperty = []
        self.ownedBeaches = []

