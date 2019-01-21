import pygame


class Board:
    def __init__(self, boardArray, path, coordinates):
        self.LINE_WIDTH = 4
        self.FIELD_LENGTH = 95
        self.texture = pygame.image.load(path)
        self.boardArray = boardArray  # READ ONLY!
        self.coordinates = coordinates

    def draw(self, screen, signs):  # signs - tuple(Sign ...)
        screen.blit(self.texture, self.coordinates)
        for player, sign in enumerate(signs, 1):
            for i in range(0, len(self.boardArray)):
                for j in range(0, len(self.boardArray[1])):
                    if (self.boardArray[i][j] == player):  # 1 - sign for first player
                        sign.draw(screen, ((i + 1) * self.LINE_WIDTH + i * self.FIELD_LENGTH + self.coordinates[0],
                                           (j + 1) * self.LINE_WIDTH + j * self.FIELD_LENGTH + self.coordinates[1]))

    def getFieldCoordinates(self, eventCoordinates):
        absCoord = (eventCoordinates[0] - self.coordinates[0], eventCoordinates[1] - self.coordinates[1])
        for j in range(0, len(self.boardArray)):
            for i in range(0, len(self.boardArray[1])):
                xi = (i + 1) * self.LINE_WIDTH + i * self.FIELD_LENGTH
                xi2 = xi + self.FIELD_LENGTH
                xj = (j + 1) * self.LINE_WIDTH + j * self.FIELD_LENGTH
                xj2 = xj + self.FIELD_LENGTH
                if (absCoord[0] > xi and absCoord[0] < xi2 and absCoord[1] > xj and absCoord[1] < xj2):
                    print("CCCCCOOOORD->", (i, j))
                    return (i, j)

        return (-1, -1)
