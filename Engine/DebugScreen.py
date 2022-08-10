from platform import platform
from Engine.Render import *
import platform
from Engine.World import *
from Engine.Player import *
from pygame import K_F3,K_p,draw

from Engine.WorldManager import WorldManager

background = Surface((2000,2000))
background.set_alpha(100)                
background.fill((0,0,0))  
class DebugScreen():
    def update(win,clock,world,GAME_NAME,GAME_VERSION,player):
        KeyPress = key.get_pressed()
        if KeyPress[K_F3]:
            win.blit(background,(0,0))
            Render.Text(Render.DebugScreenFont,f"{GAME_NAME}-{GAME_VERSION}",(255,255,255),Vector2(20,10),win)
            Render.PrintFPS(clock,win,Vector2(20,25))
            Render.Text(Render.DebugScreenFont,f"OS:{platform.system()}/{platform.machine()}",(255,255,255),Vector2(20,40),win)
            Render.Text(Render.DebugScreenFont,f"Client:{platform.python_implementation().capitalize()}/{platform.python_version()}",(255,255,255),Vector2(20,55),win)
            Render.Text(Render.DebugScreenFont,f"XY:{round((world.getWorldXZero()-player.rect.x)*-1)},{round((world.getWorldYZero()-player.rect.y)*-1)}",(255,255,255),Vector2(20,85),win)
            Render.Text(Render.DebugScreenFont,f"WorldID:{WorldManager.worldID}",(255,255,255),Vector2(20,115),win)
            if KeyPress[K_p]:
                draw.rect(win,(255,0,0),world.leftRect)
                draw.rect(win,(255,0,0),world.topRect)
                draw.rect(win,(255,0,0),world.bottomRect)
                draw.rect(win,(255,0,0),world.rightRect)