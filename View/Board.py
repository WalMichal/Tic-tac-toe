import pygame
class Board:
    def __init__(self,boardArray,path ,coordinates):
        self.LINE_WIDTH = 4
        self.FIELD_LENGTH = 95
        self.texture = pygame.image.load(path)
        self.boardArray = boardArray
        self.coordinates = coordinates
    def draw(self,screen,signs): #signs - tuple(Sign ...)
        screen.blit(self.texture,self.coordinates)
        for player,sign in enumerate(signs,1):
            for i in self.board.shape[0]:
                for j in self.board.shape[1]:
                    if(self.board[i][j] == player): #1 - sign for first player
                        sign.draw(screen,((i+1)*self.LINE_WIDTH+i*self.FIELD_LENGTH,(j+1)*self.LINE_WIDTH+j*self.FIELD_LENGTH))
    def getBoardArray(self):
        return self.boardArray
    def

kr = (1,2,312,4)
for iz,x in enumerate(kr,1):
    print(iz,' ',x)