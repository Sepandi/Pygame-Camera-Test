from Engine.Window import *
Window.INIT()
#--Initializes-game
GAME_NAME = "RPG"
GAME_VERSION = "Under Developement"
Window.INIT()
win = Window.WinInit(f"{GAME_NAME} Game by Sepandi-{GAME_VERSION}",800,600)
#--import-engine-modules
from Engine.Render import *
from Engine.DebugScreen import *
from Engine.GameTime import *
from Engine.Player import *
from Engine.World import *
from Engine.Mouse import *
from Engine.Portal import *
from Engine.Button import *
from Engine.WorldManager import WorldManager
from pygame import K_ESCAPE, image ,transform,key
#--Initializes-clock
clock = Clock()
#--Initializes-The-Worlds
world = World(win)
world.originX = 734
world.originY = 320
#--Initializes-The-Player
player = Player(win.get_width()/2-16,win.get_height()/2-16)
#--Initializes-The-Mouse-Object
mouse = Mouse()
#--Initializes-The-Portal-For-The-Camp
portal = Portal()

#--Button-Images
button1 = transform.scale(image.load("Data/Assets/UI/Button1.png").convert_alpha(),(16*4,11*4))


while Window.WindowIsRunning():
    print(key.get_mods())
    if key.get_pressed()[K_ESCAPE]:
        Window.CloseWindowManually()

    
    #--Important-Stuff-1/2
    Window.HandleEvents(win,player)
    
    #--Game-Updates
    #--on-Main-Menu
    if WorldManager.menu == 0:
        world.color = (36,137,199)
        Button.Button(x =(win.get_width()/2)-(button1.get_width()/2) ,y = 30, text = "Start",image = button1,textColor= (0,0,0),function = WorldManager.goCamp ,win = win , mouse = mouse) 
        Button.Button(x =(win.get_width()/2)-(button1.get_width()/2) ,y = win.get_height()-70, text = "Exit",image = button1,textColor= (0,0,0),function = Window.CloseWindowManually ,win = win , mouse = mouse)
    elif WorldManager.menu == 1:
        #--On-Camp
        if WorldManager.worldID == 0:
            world.color = (0,0,0)
            world.Update(win)
            portal.Update(win,world)
            player.Update(win,world)
            Button.Button(x = 10,y = 10, text = "Exit",image = button1,textColor= (0,0,0),function = WorldManager.goMainMenu ,win = win , mouse = mouse)  
    

    #--Important-Stuff-2/2
    mouse.Update(win)
    if WorldManager.menu == 1:
        DebugScreen.update(win,clock,world,GAME_NAME,GAME_VERSION,player)
    Window.Update(win,world.color)
    GameTime.SetDeltaTime(clock)
    GameTime.Update()

Window.CloseWindow()
