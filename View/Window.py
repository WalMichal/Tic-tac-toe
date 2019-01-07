import pygame
class Window:
    def __init__(self):
        pygame.init()
        self.RESOLUTION = (600, 600)
        self.BACKGROUND_COLOR = (172, 122, 51)
        self.BLACK_COLOR = (0, 0, 0)
        self.GREEN_COLOR = (0, 128, 0)
        self.boardCoordinates = (150, 200)
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        pygame.display.set_caption('Kółko i krzyżyk')
        icon = pygame.image.load('E:/Pythonidae/venv/icon.png')
        pygame.display.set_icon(icon)
        #self.startView = sv.StartView(boardArray,boardPath,signsPaths)
        #self.EndView = ev.EndView()
    ###def draw(self,P1Turn):
    def draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)
    def update(self,param):
        pass


