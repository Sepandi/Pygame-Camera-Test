from pygame import display,image,WINDOWRESIZED,QUIT,HWSURFACE,DOUBLEBUF,RESIZABLE,init,quit,time,event,mouse
#--makes-pygame-easier
class Window():
    running = True
	#--Initializes-pygame
    def INIT():
        init()
    #--Makes-a-window-also-returns-window-for-(win.blit)
    def WinInit(WindowName:str,width:int,height:int):
        win = display.set_mode((width,height),HWSURFACE|DOUBLEBUF|RESIZABLE,64)
        display.set_caption(WindowName)
        display.set_icon(image.load("Data/icon.png"))
        #--Hide-the-mouse-cursor
        mouse.set_visible(0)
        return win
    #--Closes-the-window-when-window-close-button-get-pressed(REQUAIERD)
    def HandleEvents(window,player):
        for e in event.get():
            if e.type == QUIT:
                Window.running = False
            if e.type == WINDOWRESIZED:
                # Updates Player Rects when window get resized
                player.ResetRects(window)
               
    #--Updates-The-Window(REQUAIERD)
    def Update(win,Color):
        display.update()
        win.fill(Color)

    #--Check-if-Window-is-Running
    def WindowIsRunning():
        return Window.running

    def CloseWindowManually():
        Window.running = False

    def CloseWindow():
        quit()


        

#--Makes-a-pygame-clock
class Clock():
    def __init__(self):
        self.clock = time.Clock()
    #-returns-FPS
    def getFPS(self):
        return self.clock.get_fps()
