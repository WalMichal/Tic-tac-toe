import pygame
from View import Text
from View import Board
from View import Sign
class StartView:
    def __init__(self,boardArray,boardPath,boardCoordinates,signsPaths):
        self.RESOLUTION = (600,600)
        self.BACKGROUND_COLOR = (172,122,51)
        self.BLACK_COLOR = (0,0,0)
        self.GREEN_COLOR = (0,128,0)
        #self.textPlayerTurn = Text("Ruch gracza ",30,self.GREEN_COLOR)
        self.textPlayer1 = Text("Ruch gracza pierwszego:",30,self.GREEN_COLOR)
        self.textSign1 = Text("O",30,self.BLACK_COLOR)
        self.textPlayer2 = Text("Ruch gracza drugiego", 30, self.GREEN_COLOR)
        self.textSign2 = Text("X",30,self.BLACK_COLOR)
        self.textFirstWidth =self.textPlayer1.getLength+self.textSign1.getLength()
        self.textSecondWidth =self.textPlayer2.getLength+self.textSign2.getLength()
        pygame.init()
        pygame.display.set_caption('Kółko i krzyżyk')
        icon = pygame.image.load('E:/Pythonidae/venv/icon.png')
        pygame.display.set_icon(icon)
        self.screen = pygame.display.set_mode(self.RESOLUTION)
        self.board = Board(boardArray, boardPath, boardCoordinates)
        self.nought = Sign(self.screen,signsPaths[0])
        self.cross = Sign(self.screen,signsPaths[1])

    def draw(self,P1Turn):
        self.screen.fill(self.BACKGROUND_COLOR)
        self.board.draw(self.screen,(self.nought, self.cross))
        if(P1Turn):
            self.textPlayer1.draw(self.screen,(self.RESOLUTION[1]/2-self.textFirstWidth,80))
            self.textSign1.draw(self.screen,(self.RESOLUTION[1]/2+self.textPlayer1.getLength(),80))
        else:
            self.textPlayer2.draw(self.screen, (self.RESOLUTION[1] / 2 - self.textSecondWidth, 80))
            self.textSign2.draw(self.screen, (self.RESOLUTION[1] / 2 + self.textPlayer2.getLength(), 80))
        pygame.display.flip()


