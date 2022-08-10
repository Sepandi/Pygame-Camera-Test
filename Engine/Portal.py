from pygame import image,transform,Vector2
from Engine.GameTime import GameTime
from Engine.World import *

class Portal:
    def __init__(self):
        #--Portal-Animation-Inits
        self.animationDelay = 4
        self.animationTimer = 0.48
        self.currentFrame = 1
        self.animationFrames = []
        self.imageSize = Vector2(22,32)
        for i in range(6):
            self.animationFrames.append(transform.scale(image.load(f"Data/Assets/Portal/portal{i+1}.png").convert_alpha(),(self.imageSize.x*4,self.imageSize.y*4)))

        
        #--Portal-Light-Animation-Inits
        self.lightImageSize = Vector2(67,17)
        self.lightAnimationFrames = []
        for i in range(2):
            self.lightAnimationFrames.append(transform.scale(image.load(f"Data/Assets/Portal/Portal-Lights/2PortalLights{i+1}.png").convert_alpha(),(22*4,37*4)))
        self.lightCurrentFrame = 1
        
        
    def Update(self,win,world:World):
        #--Sets-And-Reset-Animation-Timer
        self.animationTimer -= GameTime.deltaTime
        if self.animationTimer <= 0:
            self.animationTimer = 0.24*self.animationDelay
        #--Run-Portal's-And-It's-Light-Animation-Loops
        self.Animation()
        self.LightAnimation()

        #--Renders-Portal-And-It's-Light
        win.blit(self.animationFrames[self.currentFrame-1],(world.getWorldXZero()+352*2,world.getWorldYZero()-32*4))
        win.blit(self.lightAnimationFrames[self.lightCurrentFrame-1],((world.getWorldXZero()+352*2,world.getWorldYZero()-32*4)))
        
    #--Portal's-Animation-Module
    def Animation(self):
        if self.animationTimer >= 0*self.animationDelay and self.animationTimer <= 0.04*self.animationDelay:
            self.currentFrame = 1
        elif self.animationTimer >= 0.04*self.animationDelay and self.animationTimer <= 0.08*self.animationDelay:
            self.currentFrame = 2
        elif self.animationTimer >= 0.08*self.animationDelay and self.animationTimer <= 0.12*self.animationDelay:
            self.currentFrame = 3
        elif self.animationTimer >= 0.12*self.animationDelay and self.animationTimer <= 0.16*self.animationDelay:
            self.currentFrame = 4
        elif self.animationTimer >= 0.16*self.animationDelay and self.animationTimer <= 0.20*self.animationDelay:
            self.currentFrame = 5
        elif self.animationTimer >= 0.20*self.animationDelay and self.animationTimer <= 0.24*self.animationDelay:
            self.currentFrame = 6

    
    #--Portal's-Light-Animation-Module
    def LightAnimation(self):
        if self.animationTimer >= 0*self.animationDelay and self.animationTimer <= 0.12*self.animationDelay:
            self.lightCurrentFrame = 1
        elif self.animationTimer >= 0.12*self.animationDelay and self.animationTimer <= 0.24*self.animationDelay:
            self.lightCurrentFrame = 2
            