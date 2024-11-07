from Cards.Card import Card
from Player import Player
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
            "Go directly to Go (Collect 500 000)",
        ]

    def action(self, player:Player):
        card = random.randint(0,len(self.simple_chance_cards) - 1)

        if card == 0:player.money += 50
        elif card == 1:player.money += 100
        elif card == 2:player.money -=50
        elif card ==3 :player.money -=100
        elif card == 4:
            player.position +=3

        elif card == 5:
            player.position -=3

        elif card == 6:
            player.inJail = True

        elif card == 7:
            player.hasJailCard = True

        elif card == 8:
            player.position = 0
            player.money += 500000

        print(f"You Picked Card:{self.simple_chance_cards[card]}")
        input("Are you Ready To Continue? y/y:")