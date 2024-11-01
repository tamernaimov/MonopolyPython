from random import choice

from Cards.Card import Card
from Space import Space

import random


class ChanceCard(Card,Space):

    def __init__(self):
        self.simple_chance_cards = [
            "Collect $50",
            "Collect $100",
            "Pay $50",
            "Pay $100",
            "Move forward 3 spaces",
            "Move backward 3 spaces",
            "Go to Jail",
            "Get Out of Jail Free",
            "Go directly to Go (Collect $200)",
        ]
    def showCard(self):
        pass

    def action(self, player):
        card = random.randint(0,len(self.simple_chance_cards))
        print(card)

        if card == 0:player.money += 50
        elif card == 1:player.money += 100
        elif card == 2:player.money -=50
        elif card ==3 :player.money -=100
        elif card == 4:
            player.position +=3

        elif card == 5:
            player.position -=3

        elif card == 7:
            player.position = 0
            player.money += 500000

        print(self.simple_chance_cards[card])