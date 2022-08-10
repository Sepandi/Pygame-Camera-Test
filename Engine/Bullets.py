from pygame import Rect,draw,mouse,image,transform
from Engine.Render import *
from Engine.World import World
class Bullet: 
    def __init__(self):
        self.rect = Rect(0, 0,32,32)
        self.speed = 15
        self.onTheGo = False
        self.shooted = False
        self.isRendered = False
        self.movementDirection = None
        self.image = transform.scale(image.load("Data/Assets/Player/bullet.png").convert_alpha(),(8*2,8*2))
        self.angle = 0
        


    def update(self,win,shootRangeRectList,world:World,PlayerPos,playerLookingStatus):
        if mouse.get_pressed() == (1,0,0):
            self.onTheGo = True
            if not self.shooted:
                # When Launched
                self.isRendered = True

                self.shooted = True
                self.movementDirection = playerLookingStatus
                if self.movementDirection == "up":
                    self.angle = 270
                    self.rect.x = PlayerPos.x
                    self.rect.y = PlayerPos.y
                elif self.movementDirection == "down":
                    self.angle = 90
                    self.rect.x = PlayerPos.x+2
                    self.rect.y = PlayerPos.y+50
                elif self.movementDirection == "right":
                    self.angle = 0
                    self.rect.x = PlayerPos.x+20
                    self.rect.y = PlayerPos.y+25
                elif self.movementDirection == "left":
                    self.angle = 180
                    self.rect.x = PlayerPos.x
                    self.rect.y = PlayerPos.y+25
        # Checks for collision for each detector
        for x in range(4):
            if self.rect.colliderect(shootRangeRectList[x]):
                self.reload()
        for x in range(4):
            if self.rect.colliderect(world.wallRects[x]):
                self.isRendered = False
        # Moves the Bullet
        if self.onTheGo:
            if self.movementDirection == "up":
                self.rect.y -= self.speed
            if self.movementDirection == "down":
                self.rect.y += self.speed
            if self.movementDirection == "right":
                self.rect.x += self.speed
            if self.movementDirection == "left":
                self.rect.x -= self.speed
                

        if self.onTheGo and self.isRendered:    
            #draw.rect(win,(255,0,0),self.rect)
            win.blit(transform.rotate(self.image,self.angle),(self.rect.x,self.rect.y))

    # Reloads The Gun
    def reload(self):
        self.rect = Rect(-32,-32,32,32)
        self.onTheGo=False
        self.shooted = False
        self.isRendered = False



        

