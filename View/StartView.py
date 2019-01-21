import pygame
from View import Text as t
from View import Board as b
from View import Sign as s
from View import Window as w


class StartView(w.Window):
    def __init__(self, board_array, board_path, signs_paths):
        w.Window.__init__(self)

        self.__text_player1 = t.Text("Ruch gracza pierwszego:", 30, self.GREEN_COLOR)
        self.__text_sign1 = t.Text("O", 30, self.BLACK_COLOR)
        self.__text_player2 = t.Text("Ruch gracza drugiego:", 30, self.GREEN_COLOR)
        self.__text_sign2 = t.Text("X", 30, self.BLACK_COLOR)
        self.__text_first_width = self.__text_player1.get_length() + self.__text_sign1.get_length()
        self._text_second_width = self.__text_player2.get_length() + self.__text_sign2.get_length()
        self._board_coordinates = (150, 200)
        self.__p1_turn = True

        self.__board = b.Board(board_array, board_path, self._board_coordinates)
        self.__nought = s.Sign(signs_paths[0])
        self.__cross = s.Sign(signs_paths[1])

    def draw(self):
        super(StartView, self).draw()
        self.__board.draw(self.screen, (self.__nought, self.__cross))
        if self.__p1_turn:
            self.__text_player1.draw(self.screen, (self.RESOLUTION[1] / 2 - self.__text_first_width / 2, 80))
            self.__text_sign1.draw(self.screen, (self.RESOLUTION[1] / 2 + self.__text_player1.get_length() / 2, 80))
        else:
            self.__text_player2.draw(self.screen, (self.RESOLUTION[1] / 2 - self._text_second_width / 2, 80))
            self.__text_sign2.draw(self.screen, (self.RESOLUTION[1] / 2 + self.__text_player2.get_length() / 2, 80))
        pygame.display.flip()

    def get_field_coordinates(self, coordinates):
        return self.__board.getFieldCoordinates(coordinates)

    def update_player_turn(self, p1_turn):
        self.__p1_turn = p1_turn
