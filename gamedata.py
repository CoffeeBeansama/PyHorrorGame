import pygame as pg

class Game:
    def __init__(self,id):
        self.id = id

        self.playerPos = [(100,100),(150,100)]

        

    
    def updatePlayerOnePos(self,pos):
        
        self.playerPos[0] = pos

     
    
    def updatePlayerTwoPos(self,pos):
        self.playerPos[1] = pos
 

    def getPlayerOnePos(self):
        return self.playerPos[0]
    
    def getPlayerTwoPos(self):
        return self.playerPos[1]