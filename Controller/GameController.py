import pygame
from Model import GameModel as g
from View import StartView as v
from View import EndView as ev
from View import Window as w
from pathlib import Path
import os.path


class GameController:
    def __init__(self):
        self.gameModel = g.GameModel()
        self.statusInfo = 0
        # 0 - startView screen
        # 1 - endView screen
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path = os.path.normpath(my_path).replace('\\', '/').replace("Controller", "View")

        while True:
            self.startView = v.StartView(self.gameModel.getBoard(),
                                         my_path + '/board-texture.png', (
                                             my_path + '/nought.png',
                                             my_path + '/cross.png'))

            while not (self.gameModel.getResult()):
                self.startView.update_player_turn(self.gameModel.ifFirstPlayerTurn())
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
                if not (self.statusInfo):
                    self.gameModel.insertSign(self.startView.get_field_coordinates(mouseCoord))
                else:
                    if self.endView.getOption(mouseCoord) == 2:
                        exit()
                    if self.endView.getOption(mouseCoord) == 1:
                        self.gameModel.init()
                        self.statusInfo = 0


GameController()
