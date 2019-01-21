import pygame
import os.path

class Window:
    def __init__(self):
        pygame.init()
        self.RESOLUTION = (600, 600)
        self.BACKGROUND_COLOR = (172, 122, 51)
        self.BLACK_COLOR = (0, 0, 0)
        self.GREEN_COLOR = (0, 128, 0)

        self.screen = pygame.display.set_mode(self.RESOLUTION)
        pygame.display.set_caption('Kółko i krzyżyk')
        my_path = os.path.abspath(os.path.dirname(__file__))
        my_path = os.path.normpath(my_path).replace('\\', '/')

        self.icon = pygame.image.load(my_path+'/icon.png')
        pygame.display.set_icon(self.icon)

    def draw(self):
        self.screen.fill(self.BACKGROUND_COLOR)
