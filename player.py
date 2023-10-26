import pygame as pg
from support import import_folder





class Player(pg.sprite.Sprite):
    def __init__(self,pos,group):
        super().__init__(group)

        self.pos = pos

        self.spritePath = "Sprites/Player/"

        self.importSprites()

        self.image = pg.image.load(f"{self.spritePath}Down_idle/00.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.hitbox = self.rect.inflate(0,0)

        self.direction = pg.math.Vector2()

        self.state = "Down_idle"
     

        self.walkingAnimationTime = 1 / 8
        self.frame_index = 0

        self.speed = 1
        

    
    def importSprites(self):
        self.animationStates = {
            "Down": [],"Left": [], "Up": [] , "Right": [],
            "Down_idle": [], "Left_idle": [], "Right_idle": [], "Up_idle": []
        }

        for animations in self.animationStates.keys():
            fullPath = self.spritePath + animations
            self.animationStates[animations] = import_folder(fullPath)


    def handleMovement(self,speed):
        self.hitbox.x += self.direction.x * speed
        self.hitbox.y += self.direction.y * speed

        self.rect.center = self.hitbox.center
    

    def idleState(self):
        self.direction.x = 0
        self.direction.y = 0

        if not "idle" in self.state:
            self.state = f"{self.state}_idle"


    def handleHorizontalDirection(self,x,state):
        self.direction.x = x
        self.direction.y = 0
        self.state = state

    def handleVerticalDirection(self,y,state):
        self.direction.x = 0
        self.direction.y = y
        self.state = state
    
    def handleAnimation(self):
        animation = self.animationStates[self.state]
        self.frame_index += self.walkingAnimationTime

        if self.frame_index >= len(animation):
            self.frame_index = 0 

        self.image = animation[int(self.frame_index)].convert_alpha()
        self.rect = self.image.get_rect(center=self.hitbox.center)


    def getInputs(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.handleVerticalDirection(-1,"Up")
        elif keys[pg.K_s]:
            self.handleVerticalDirection(1,"Down")
        elif keys[pg.K_a]:
            self.handleHorizontalDirection(-1,"Left")
        elif keys[pg.K_d]:
            self.handleHorizontalDirection(1,"Right")
        else:
            self.idleState()

        
    def update(self):
        self.getInputs()
        self.handleMovement(self.speed)
        self.handleAnimation()
