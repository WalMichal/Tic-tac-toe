import pygame
from View import Text as t
from View import Window as w


class EndView(w.Window):
    def __init__(self, game_result):
        w.Window.__init__(self)
        self.FIGURE_WIDTH = 3
        self.REC_HEIGHT = 50
        self.REC_WIDTH = 300
        self.REC_ONCE_AGAIN_COORD = (150, 250)
        self.REC_END_COORD = (150, 310)
        if game_result == 1:
            self.__text_result = t.Text("Wygrał gracz pierwszy!", 40, self.GREEN_COLOR)
        else:
            if game_result == 2:
                self.__text_result = t.Text("Wygrał gracz drugi!", 40, self.GREEN_COLOR)
            else:
                if game_result == 3:
                    self.__text_result = t.Text("Remis", 40, self.GREEN_COLOR)
                else:
                    self.__text_result = t.Text("Koniec gry", 40, self.GREEN_COLOR)
        self.__text_play_again = t.Text("Zagraj jeszcze raz.", 30, self.BLACK_COLOR)
        self.__text_end = t.Text("Zamknij.", 30, self.BLACK_COLOR)

        self.__rec_once_again = pygame.Rect(self.REC_ONCE_AGAIN_COORD[0], self.REC_ONCE_AGAIN_COORD[1], self.REC_WIDTH,
                                            self.REC_HEIGHT)
        self.__rec_end = pygame.Rect(self.REC_END_COORD[0], self.REC_END_COORD[1], self.REC_WIDTH, self.REC_HEIGHT)

    def draw(self):
        super(EndView, self).draw()
        pygame.draw.rect(self.screen, (0, 128, 0), self.__rec_once_again, self.FIGURE_WIDTH)
        pygame.draw.rect(self.screen, (0, 128, 0), self.__rec_end, self.FIGURE_WIDTH)
        x = self.REC_WIDTH / 2 - self.__text_play_again.get_length() / 2 + self.REC_ONCE_AGAIN_COORD[0]
        y = self.REC_HEIGHT / 2 - self.__text_play_again.get_heigth() / 2 + self.REC_ONCE_AGAIN_COORD[1]
        self.__text_play_again.draw(self.screen, (x, y))
        x = self.REC_WIDTH / 2 - self.__text_end.get_length() / 2 + self.REC_END_COORD[0]
        y = self.REC_HEIGHT / 2 - self.__text_end.get_heigth() / 2 + self.REC_END_COORD[1]
        self.__text_end.draw(self.screen, (x, y))
        self.__text_result.draw(self.screen, (self.RESOLUTION[0] / 2 - self.__text_result.get_length() / 2, 80))

        pygame.display.flip()

    def getOption(self, coordinates):
        # 0 - not clicking in options
        # 1 - option "Play again"
        # 2 - option "End"
        if self.__rec_end.collidepoint(coordinates):
            return 2
        if self.__rec_once_again.collidepoint(coordinates):
            return 1
        return 0
