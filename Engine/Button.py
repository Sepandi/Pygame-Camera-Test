from pygame import draw , Rect
from pygame import mouse as mouseModule
from Engine.Render import *

class Button:
    def Button(x,y,text,image:Surface,textColor,function,win,mouse):
        rect = Rect(x,y,image.get_width(),image.get_height())
        text = Render.Bold.render(text,True,textColor)
        if mouse.rect.colliderect(rect):
            draw.rect(win,(255,255,255),Rect(x-2,y-2,4+rect.width,4+rect.height))
        win.blit(image,(x,y))
        win.blit(text,(x+(image.get_width()/2)-(text.get_width()/2),y+(image.get_height()/2)-(text.get_height()/2)))

        if mouse.rect.colliderect(rect):
            if mouseModule.get_pressed() == (1,0,0):
                function()
        

        

        

