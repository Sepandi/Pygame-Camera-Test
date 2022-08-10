from pygame import image,Rect,Surface,transform,K_UP,key,K_w,K_s,K_DOWN,K_a,K_LEFT,K_d,K_RIGHT,Vector2,draw
from Engine.GameTime import GameTime
from Engine.World import *
from Engine.Bullets import *
class Player():
    def __init__(self,x,y):
        # Health
        self.health = 10
        # Rectangle
        self.rect = Rect(x, y, 32, 64)

        # Gun Related things (Range,Detectors and Their Lists)
        self.shootRange = 200
        self.shootRangeRectUp = Rect(self.rect.x,self.rect.y-self.shootRange-64,32,64)
        self.shootRangeRectDown = Rect(self.rect.x,self.rect.y+self.rect.height+self.shootRange,32,64)
        self.shootRangeRectRight = Rect(self.rect.x+self.rect.width+self.shootRange,self.rect.y,64,32)
        self.shootRangeRectLeft = Rect(self.rect.x-self.shootRange-64,self.rect.y,64,32)
        self.shootRangeRectList = [self.shootRangeRectUp,self.shootRangeRectDown,self.shootRangeRectRight,self.shootRangeRectLeft ]
        # Player rects to detect collision 
        self.rightRect = Rect(self.rect.x+32, self.rect.y, 5, 69)
        self.leftRect = Rect(self.rect.x-5, self.rect.y, 5, 69)
        self.topRect = Rect(self.rect.x, self.rect.y, 32, 5)
        self.buttomRect = Rect(self.rect.x, self.rect.y+64, 32, 5)

        # Player Speed
        self.speed = 5

        # Things for Player Animation
        self.moving = False
        self.facingStatus = "down"
        self.facingRight = True
        self.shadow = image.load("Data/Assets/Player/shadow.png")
        self.animationFrame = []
        for x in range(12):
            self.animationFrame.append(image.load("Data/Assets/Player/RightLeft/PlayerRunning/PlayerRunning"+str(x+1)+".png").convert_alpha())
        for x in range(2):
            self.animationFrame.append(image.load("Data/Assets/Player/RightLeft/PlayerIdle"+str(x+1)+".png").convert_alpha())
        for x in range(3):
            self.animationFrame.append(image.load("Data/Assets/Player/Down/PlayerDown"+str(x+1)+".png").convert_alpha())
        for x in range(3):
            self.animationFrame.append(image.load("Data/Assets/Player/Up/PlayerUp"+str(x+1)+".png").convert_alpha())
        self.animationTimer = 0    
        self.currentFrame = 0 

        #--Bullets-Manager
        self.bullet = Bullet()


    def ResetRects(self,window):
        self.rect = Rect(window.get_width()/2-16,window.get_height()/2-16,32,64)
        self.rightRect = Rect(self.rect.x+32, self.rect.y, 5, 69)
        self.leftRect = Rect(self.rect.x-5, self.rect.y, 5, 69)
        self.topRect = Rect(self.rect.x, self.rect.y, 32, 5)
        self.buttomRect = Rect(self.rect.x, self.rect.y+64, 32, 5)
        self.shootRangeRectList[0] = Rect(self.rect.x,self.rect.y-self.shootRange-64,32,64)
        self.shootRangeRectList[1] = Rect(self.rect.x,self.rect.y+self.rect.height+self.shootRange,32,64)
        self.shootRangeRectList[2] = Rect(self.rect.x+self.rect.width+self.shootRange,self.rect.y,64,32)
        self.shootRangeRectList[3] = Rect(self.rect.x-self.shootRange-64,self.rect.y,64,32)
        

    def Update(self,win:Surface,world:World):
        self.rightRect = Rect(self.rect.x+32, self.rect.y, 5, 69)
        self.leftRect = Rect(self.rect.x-5, self.rect.y, 5, 69)
        self.topRect = Rect(self.rect.x, self.rect.y, 32, 5)
        self.buttomRect = Rect(self.rect.x, self.rect.y+64, 32, 5)
        #--KeyBinds
        KeyPress = key.get_pressed()

        if KeyPress[K_w] or KeyPress[K_UP]:
            self.facingStatus = "up"
            self.moving = True
            world.originY -= self.speed
        elif KeyPress[K_s] or KeyPress[K_DOWN]:
            self.facingStatus = "down"
            self.moving = True
            self.facingRight = True
            world.originY += self.speed
        elif KeyPress[K_a] or KeyPress[K_LEFT]:
            self.facingStatus = "left"
            self.moving = True
            self.facingRight = False
            world.originX -= self.speed
        elif KeyPress[K_d] or KeyPress[K_RIGHT]:
            self.facingStatus = "right"
            self.moving = True
            self.facingRight = True
            world.originX += self.speed
        else:
            self.moving = False
        #--Set-Borders
        if self.leftRect.colliderect(world.leftRect):
            world.originX += self.speed
            self.moving = False
        if self.rightRect.colliderect(world.rightRect):
            world.originX -= self.speed
            self.moving = False
        if self.topRect.colliderect(world.topRect):
            world.originY += self.speed
            self.moving = False
        if self.buttomRect.colliderect(world.bottomRect):
            world.originY -= self.speed
            self.moving = False
        

        #--Gun-Updates
        self.bullet.update(win,self.shootRangeRectList,world,Vector2(self.rect.x,self.rect.y),self.facingStatus)
        

        #--Start-Draws
        self.Draw(win)

    
    def Draw(self,win:Surface):
        #--Running-Player-Animation-Component
        self.Animation()
        #--Draw-Player's-Shadow
        win.blit(self.shadow,(self.rect.x,self.rect.y+self.rect.width+25))
        #--Draw-Player-with-Facing-Check
        if self.facingRight:
            win.blit(self.animationFrame[self.currentFrame],(self.rect.x,self.rect.y,32,64))
        else:
            win.blit(transform.flip(self.animationFrame[self.currentFrame],True,False),(self.rect.x,self.rect.y,32,64))

        

    #--Player-Animation-Component
    def Animation(self):
        self.animationTimer += GameTime.deltaTime
        if self.animationTimer > 0.48:
            self.animationTimer = 0
        
        if self.moving:
            if self.facingStatus == "left" or self.facingStatus == "right":
                if self.animationTimer <= 0 and self.animationTimer <= 0.04:
                    self.currentFrame = 0
                elif self.animationTimer >= 0.04 and self.animationTimer <= 0.08:
                    self.currentFrame = 1
                elif self.animationTimer >= 0.08 and self.animationTimer <= 0.12:
                    self.currentFrame = 2
                elif self.animationTimer >= 0.12 and self.animationTimer <= 0.16:
                    self.currentFrame = 3
                elif self.animationTimer >= 0.16 and self.animationTimer <= 0.20:
                    self.currentFrame = 4
                elif self.animationTimer >= 0.20 and self.animationTimer <= 0.24:
                    self.currentFrame = 5
                elif self.animationTimer >= 0.24 and self.animationTimer <= 0.28:
                    self.currentFrame = 6
                elif self.animationTimer >= 0.28 and self.animationTimer <= 0.32:
                    self.currentFrame = 7
                elif self.animationTimer >= 0.32 and self.animationTimer <= 0.36:
                    self.currentFrame = 8
                elif self.animationTimer >= 0.36 and self.animationTimer <= 0.40:
                    self.currentFrame = 9
                elif self.animationTimer >= 0.40 and self.animationTimer <= 0.44:
                    self.currentFrame = 10
                elif self.animationTimer >= 0.44 and self.animationTimer <= 0.48:
                    self.currentFrame = 11
            
            if self.facingStatus == "down":
                if self.animationTimer <= 0 and self.animationTimer <= 0.12:
                    self.currentFrame = 15
                elif self.animationTimer >= 0.12 and self.animationTimer <= 0.24:
                    self.currentFrame = 16
                elif self.animationTimer >= 0.24 and self.animationTimer <= 0.36:
                    self.currentFrame = 15
                elif self.animationTimer >= 0.36 and self.animationTimer <= 0.48:
                    self.currentFrame = 16


                
            if self.facingStatus == "up":
                if self.animationTimer <= 0 and self.animationTimer <= 0.12:
                    self.currentFrame = 18
                elif self.animationTimer >= 0.12 and self.animationTimer <= 0.24:
                    self.currentFrame = 19
                elif self.animationTimer >= 0.24 and self.animationTimer <= 0.36:
                    self.currentFrame = 18
                elif self.animationTimer >= 0.36 and self.animationTimer <= 0.48:
                    self.currentFrame = 19
        else:
            if self.facingStatus == "right" or self.facingStatus == "left":
                if self.animationTimer <= 0 and self.animationTimer <= 0.24:
                    self.currentFrame = 12
                elif self.animationTimer >= 0.24 and self.animationTimer <= 0.48:
                    self.currentFrame = 13
                if self.facingStatus == "down":
                    self.currentFrame = 14
                if self.facingStatus == "up":
                    self.currentFrame = 17

        if not self.moving:
            if self.facingStatus == "right" or self.facingStatus == "left":
                if self.animationTimer <= 0 and self.animationTimer <= 0.24:
                    self.currentFrame = 12
                elif self.animationTimer >= 0.24 and self.animationTimer <= 0.48:
                    self.currentFrame = 13
            if self.facingStatus == "down":
                self.currentFrame = 14
            if self.facingStatus == "up":
                self.currentFrame = 17
