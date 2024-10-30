from Cards.Card import Card
from Space import Space


class ChanceCard(Card,Space):

    def showCard(self):
        pass
    def action(self, player):
        print("CHANCE CARD ACTION!")
