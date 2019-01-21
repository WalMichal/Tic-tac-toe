import pygame
from Model import GameModel as g
from View import StartView as v
from View import EndView as ev
import os.path


class GameController:
    def __init__(self):
        self.__game_model = g.GameModel()
        self.__view_info = 0
        # 0 - startView screen
        # 1 - endView screen
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path = os.path.normpath(my_path).replace('\\', '/').replace("Controller", "View")

        while True:
            self.__start_view = v.StartView(self.__game_model.get_board(),
                                            my_path + '/board-texture.png', (
                                             my_path + '/nought.png',
                                             my_path + '/cross.png'))

            while not (self.__game_model.get_result()):
                self.__start_view.update_player_turn(self.__game_model.if_first_player_turn())
                self.__start_view.draw()
                self.events()
            self.__view_info = 1
            self.__end_view = ev.EndView(self.__game_model.get_result())
            while self.__view_info == 1:
                self.__end_view.draw()
                self.events()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_coord = pygame.mouse.get_pos()
                if not self.__view_info:
                    self.__game_model.insert_sign(self.__start_view.get_field_coordinates(mouse_coord))
                else:
                    if self.__end_view.getOption(mouse_coord) == 2:
                        exit()
                    if self.__end_view.getOption(mouse_coord) == 1:
                        self.__game_model.init()
                        self.__view_info = 0


GameController()
