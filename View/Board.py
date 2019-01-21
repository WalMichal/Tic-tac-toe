import pygame


class Board:
    def __init__(self, boardArray, board_path, coordinates):
        self.__LINE_WIDTH = 4
        self.__FIELD_LENGTH = 95
        self.__texture = pygame.image.load(board_path)
        self.__BOARD_ARRAY = boardArray  # READ ONLY!
        self.__coordinates = coordinates  #board coord

    def draw(self, screen, signs):  # signs - tuple(Sign ...)
        screen.blit(self.__texture, self.__coordinates)
        for player, sign in enumerate(signs, 1):
            for i in range(0, len(self.__BOARD_ARRAY)):
                for j in range(0, len(self.__BOARD_ARRAY[1])):
                    if (self.__BOARD_ARRAY[i][j] == player):  # 1 - sign for first player
                        sign.draw(screen, ((i + 1) * self.__LINE_WIDTH + i * self.__FIELD_LENGTH + self.__coordinates[0],
                                           (j + 1) * self.__LINE_WIDTH + j * self.__FIELD_LENGTH + self.__coordinates[1]))

    def getFieldCoordinates(self, event_coordinates):
        abs_coord = (event_coordinates[0] - self.__coordinates[0], event_coordinates[1] - self.__coordinates[1])
        for j in range(0, len(self.__BOARD_ARRAY)):
            for i in range(0, len(self.__BOARD_ARRAY[1])):
                xi = (i + 1) * self.__LINE_WIDTH + i * self.__FIELD_LENGTH
                xi2 = xi + self.__FIELD_LENGTH
                xj = (j + 1) * self.__LINE_WIDTH + j * self.__FIELD_LENGTH
                xj2 = xj + self.__FIELD_LENGTH
                if (abs_coord[0] > xi and abs_coord[0] < xi2 and abs_coord[1] > xj and abs_coord[1] < xj2):
                    return (i, j)

        return (-1, -1)  #no field has been clicked
