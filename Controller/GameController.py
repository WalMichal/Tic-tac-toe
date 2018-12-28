import pygame
from Model import GameModel
from View import StartView as v
class GameController:
    def __init__(self):
        self.startView = v.StartView()
        self.gameModel = GameModel()
        while not(self.gameModel.checkIfWin()) or not(self.gameModel.checkIfDraw()):
            self.startView.draw(self.gameModel.ifFirstPlayerTurn())
            self.events()
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

a = GameController()
