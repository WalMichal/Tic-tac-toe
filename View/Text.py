import pygame
class Text:
    def __init__(self,text,size,color):
        self.font = pygame.font.SysFont("comicsansms", size, 1)
        self.text = self.font.render(text, True, color)
    def draw(self,screen ,coordinates):
        screen.blit(self.text,coordinates)
    def getLength(self):
        return self.text.get_rect().width
    def getHeigth(self):
        return self.text.get_rect().height



