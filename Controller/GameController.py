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
        self.window = w.Window()
        self.lastStatusInfo = -1
        while True:
            self.changeStatus()
            self.window.update(self.gameModel.ifFirstPlayerTurn())
            self.window.draw()
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
                    if(self.gameModel.getResult() != 0):
                        self.statusInfo = 1
                else:
                    if self.endView.getOption(mouseCoord)== 2:
                        exit()
                    if self.endView.getOption(mouseCoord) == 1:
                        self.gameModel.init()
                        self.statusInfo = 0
    def changeStatus(self):
        if(self.lastStatusInfo != self.statusInfo):
            if(self.statusInfo == 0):
                self.window = v.StartView(self.gameModel.getBoard(),
                                          'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/board-texture.png', (
                                              'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/nought.png',
                                              'C:/Users/Drewno/Desktop/IO/IO-Spec/grafika/cross.png'))
            else:
                self.window = ev.EndView()


GameController()
