class Map():
    def __init__(self):
        from Properties.Beach import Beach
        from Properties.PropertyFactory import PropertyFactory
        from Cards.ChanceCard import ChanceCard
        from MakeMonopoly import MakeMonopoly
        from Jail import Jail
        from WorldTour import WorldTour
        from Start import Start
        self.cc = ChanceCard()
        self.makeMonopoly = MakeMonopoly()
        self.jail = Jail()
        self.worldTour = WorldTour()
        self.start = Start()
        self.space = [
                      Start(),
                      PropertyFactory("Grenada", 5000, 2000,  "Spain", "Land").createB(),
                      PropertyFactory("Seville", 2000, 3000,  "Spain", "Land").createB(),
                      PropertyFactory("Madrid", 3000, 200,  "Spain", "Land").createB(),
                      Beach("Bali", 3000, 200),
                      PropertyFactory("Hong Kong", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Beijing", 3000, 200,  "China", "Land").createB(),
                      PropertyFactory("Shanghai", 3000, 200,  "China", "Land").createB(),
                      self.jail,
                      PropertyFactory("Venice", 3000, 200,  "Italy", "Land").createB(),
                      PropertyFactory("Milan", 3000, 200,  "Italy", "Land").createB(),
                      PropertyFactory("Rome", 3000, 200,  "Italy", "Land").createB(),
                      self.cc,
                      PropertyFactory("Hamburg", 3000, 200,  "Germany", "Land").createB(),
                      Beach("Cyprus",3000,200),
                      PropertyFactory("Berlin", 3000, 200,  "Germany", "Land").createB(),
                      PropertyFactory("Liverpool", 3000, 200,  "England", "Land").createB(),#MAKE THIS A WORLD CHAMPIONSHIP
                      PropertyFactory("London", 3000, 200,"England", "Land").createB(),
                      Beach("Dubai",2000,200),
                      PropertyFactory("Sydney", 3000, 200,  "England", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Chicago", 3000, 200,  "USA", "Land").createB(),
                      PropertyFactory("Las Vegas", 3000, 200, "USA", "Land").createB(),
                      PropertyFactory("New York", 3000, 200,  "USA", "Land").createB(),
                      self.worldTour,
                      Beach("Nice",2000,200),
                      PropertyFactory("Lyon", 3000, 200,  "France", "Land").createB(),
                      PropertyFactory("Paris", 3000, 200,  "France", "Land").createB(),
                      ChanceCard(),
                      PropertyFactory("Osaka", 3000, 200, "Japan", "Land").createB(),
                      PropertyFactory("Tokyo", 3000, 200,  "Japan", "Land").createB(),]