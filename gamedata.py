import pygame as pg

class Game:
    def __init__(self,id):
        self.id = id

        self.playerData = [None,None]

            
    def updatePlayerOneData(self,dir):
        self.playerData[0] = dir
        
    def updatePlayerTwoData(self,dir):
        self.playerData[1] = dir 

    def getPlayerOneData(self):
        return self.playerData[0]
    
    def getPlayerTwoData(self):
        return self.playerData[1]