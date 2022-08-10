class WorldManager:
    #--(0=MainMenu , 1=Game , 2=AboutPage)--
    menu = 1
    #--(0=Camp)--
    worldID = 0

    #--World&Menu-Related-Functions-For-Buttons
    def goMainMenu():
        WorldManager.menu = 0
    def goCamp():
        WorldManager.menu = 1
        WorldManager.worldID = 0