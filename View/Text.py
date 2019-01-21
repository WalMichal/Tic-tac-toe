import pygame


class Text:
    def __init__(self, text, size, color):
        self.__font = pygame.font.SysFont("comicsansms", size, 1)
        self.__text = self.__font.render(text, True, color)

    def draw(self, screen, coordinates):
        screen.blit(self.__text, coordinates)

    def get_length(self):
        return self.__text.get_rect().width

    def get_heigth(self):
        return self.__text.get_rect().height
