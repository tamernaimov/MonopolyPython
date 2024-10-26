from Player import Player
from Properties.Land import Land
from Properties.Property import Property


class Map():
    def returnAction(self,player):
        if player.position == 3:
             Land(20000,3000,0,"Spain",False).action() #adding the land in a land list

