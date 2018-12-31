import pygame
from Model import GameModel as g
from View import StartView as v
from View import EndView as ev
from View import Window as w
class GameController:
    def __init__(self,):
        self.gameModel = g.GameModel()
        self.result = self.gameModel.getResult() #niepotrzebne :(
        self.statusInfo = 0
        #0 - first screen
        #1 - second screen
        #self.ednView = ev.EndView()
        while True:
            self.startView = v.StartView(self.gameModel.getBoard(),
                                         'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/board-texture.png', (
                                         'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/nought.png',
                                         'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/cross.png'))

            while not(self.gameModel.getResult()):
                self.startView.updatePlayerTurn(self.gameModel.ifFirstPlayerTurn())
                self.startView.draw()
                self.events()
            self.statusInfo = 1
            self.endView = ev.EndView(self.gameModel.getResult())
            while self.statusInfo == 1:
                self.endView.draw()
                self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseCoord = pygame.mouse.get_pos()
                print(mouseCoord)
                if not(self.statusInfo):
                    self.gameModel.insertSign(self.startView.getFieldCoordinates(mouseCoord))
                else:
                    if self.endView.getOption(mouseCoord)== 2:
                        exit()
                    if self.endView.getOption(mouseCoord) == 1:
                        self.gameModel.init()
                        self.statusInfo = 0


GameController()
