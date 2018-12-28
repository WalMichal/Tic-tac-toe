import pygame
class Sign:
    def __init__(self,path):
        self.texture = pygame.load(path)
    def draw(self,screen,coordinates):
        screen.blit(self.texture,coordinates)