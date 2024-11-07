import random

class DiceForJail():
    def throwDiceOutOfJail(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print()
        print(f"You Threw {a} and {b}")
        print()
        if a==b:
            return True
        else:
            return False