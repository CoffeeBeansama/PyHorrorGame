import pygame as pg

class Game:
    def __init__(self,id):
        self.id = id

        self.playerPos = [(100,100),(150,100)]
        

    
    def updatePlayerOnePos(self,pos):
        newPos = pos.replace(',',"")
        self.playerPos[0] = newPos

     
    
    def updatePlayerTwoPos(self,pos):
        newPos = pos.replace(',',"")
        self.playerPos[1] = newPos
 

    def getPlayerOnePos(self):
        return self.playerPos[0]
    
    def getPlayerTwoPos(self):
        return self.playerPos[1]