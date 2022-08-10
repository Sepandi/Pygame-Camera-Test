from pygame import image,Rect,Surface,transform
class World():
    def __init__(self,win):
        self.color = (36,137,199)
        self.worldID = 1
        self.originX = 0
        self.originY = 0
        self.worldImg = image.load("Data/Assets/World/world3.png").convert_alpha()
        self.worldImg = transform.scale(self.worldImg,(self.worldImg.get_width()*4,self.worldImg.get_height()*4))
        self.worldImgW = self.worldImg.get_width()
        self.worldImgH = self.worldImg.get_height()

        self.worldImgWall = image.load("Data/Assets/World/world3Walls.png").convert_alpha()
        self.worldImgWall = transform.scale(self.worldImgWall,(self.worldImgWall.get_width()*4,self.worldImgWall.get_height()*4))

        self.topRect = Rect(0,0,0,0)
        self.bottomRect = Rect(0,0,0,0)
        self.leftRect = Rect(0,0,0,0)
        self.rightRect = Rect(0,0,0,0)
        self.wallRects = [self.topRect,self.bottomRect,self.leftRect,self.rightRect]
        self.win = win
        self.worldXZero = (win.get_width()/2)-self.originX
        self.worldYZero = (win.get_height()/2)-self.originY

    def Update(self,win:Surface):
        
        #--Getting-Worlds-Zero-Coordinates
        self.win = win
        worldXZero = (win.get_width()/2)-self.originX
        worldYZero = (win.get_height()/2)-self.originY

        #--Getting-Worlds-Rectangles-For-Borders-(Top,Bottom,Left,Right)
        self.topRect = Rect((worldXZero-32,worldYZero-20-64,self.worldImgW+32,32))
        self.bottomRect = Rect((worldXZero-32,worldYZero+self.worldImgH,self.worldImgW+32,32))
        self.leftRect = Rect((worldXZero-32,worldYZero-64,32,self.worldImgH+64))
        self.rightRect = Rect((worldXZero+self.worldImgW,worldYZero-64,32,self.worldImgH+64))
        self.wallRects = [self.topRect,self.bottomRect,self.leftRect,self.rightRect]

        self.Draw(win)

    
    def Draw(self,win:Surface):
        win.blit(self.worldImg,((win.get_width()/2)-self.originX,(win.get_height()/2)-self.originY))
        win.blit(self.worldImgWall,((win.get_width()/2)-self.originX-64,(win.get_height()/2)-self.originY-64))
    
    #--Returns-the-X-And-Y-Coordinate-of-the-World-Zero-Point
    def getWorldXZero(self):
        return (self.win.get_width()/2)-self.originX
    def getWorldYZero(self):
        return (self.win.get_height()/2)-self.originY