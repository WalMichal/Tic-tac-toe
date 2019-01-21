import pygame


class Sign:
    def __init__(self, path):
        self.__texture = pygame.image.load(path)

    def draw(self, screen, coordinates):
        screen.blit(self.__texture, coordinates)
