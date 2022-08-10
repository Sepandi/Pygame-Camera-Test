from pygame import image,Rect,Surface,transform,draw,mouse
class Mouse:
    def __init__(self):
        self.normal = image.load("Data/Assets/UI/mouse1.png").convert_alpha()
        self.normal = transform.scale(self.normal,(self.normal.get_width()*2,self.normal.get_height()*2))
        self.clicked = image.load("Data/Assets/UI/mouse2.png").convert_alpha()
        self.clicked = transform.scale(self.clicked,(self.clicked.get_width()*2,self.clicked.get_height()*2))
        self.rect = Rect(0,0,10,10)

    def Update(self,win:Surface):
        (self.rect.x,self.rect.y) = mouse.get_pos()
        if mouse.get_pressed() != (1,0,0):  
            win.blit(self.normal,mouse.get_pos())
        elif mouse.get_pressed() == (1,0,0):
            win.blit(self.clicked,mouse.get_pos())
        