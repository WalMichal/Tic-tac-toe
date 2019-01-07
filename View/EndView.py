import pygame
from View import Text as t
import GLOBAL_DEFINE as g
from View import Window as w
class EndView(w.Window):
    def __init__(self):
        w.Window.__init__(self)
        self.FIGURE_WIDTH = 3
        self.REC_HEIGHT = 50
        self.REC_WIDTH = 300
        self.REC_ONCE_AGAIN_COORD = (150,250)
        self.REC_END_COORD = (150,310)
        self.textOnceAgain = t.Text("Zagraj jeszcze raz.",30,self.BLACK_COLOR)
        self.textEnd = t.Text("Zamknij.",30,self.BLACK_COLOR)

        self.lastGameResult = 3

        self.recOnceAgain = pygame.Rect(self.REC_ONCE_AGAIN_COORD[0], self.REC_ONCE_AGAIN_COORD[1], self.REC_WIDTH, self.REC_HEIGHT)
        self.recEnd = pygame.Rect(self.REC_END_COORD[0], self.REC_END_COORD[1], self.REC_WIDTH, self.REC_HEIGHT)

    def draw(self):
        super(EndView,self).draw()
        pygame.draw.rect(self.screen,(0,128,0),self.recOnceAgain,self.FIGURE_WIDTH)
        pygame.draw.rect(self.screen,(0,128,0),self.recEnd,self.FIGURE_WIDTH)
        x = self.REC_WIDTH/2 - self.textOnceAgain.getLength()/2 +self.REC_ONCE_AGAIN_COORD[0]
        y = self.REC_HEIGHT/2 - self.textOnceAgain.getHeigth()/2 +self.REC_ONCE_AGAIN_COORD[1]
        self.textOnceAgain.draw(self.screen,(x,y))
        x = self.REC_WIDTH / 2 - self.textEnd.getLength() / 2 + self.REC_END_COORD[0]
        y = self.REC_HEIGHT / 2 - self.textEnd.getHeigth() / 2 + self.REC_END_COORD[1]
        self.textEnd.draw(self.screen,(x,y))
        self.textResult.draw(self.screen,(self.RESOLUTION[0]/2-self.textResult.getLength()/2,80))



        pygame.display.flip()
    def getOption(self,coordinates):
        #0 - not clicking in options
        #1 ption "Play againa"
        #2 option "End"
        if self.recEnd.collidepoint(coordinates):
            return 2
        if self.recOnceAgain.collidepoint(coordinates):
            return 1
        return 0
    def update(self,gameResult):
        if gameResult!= self.lastGameResult:
            self.lastGameResult = gameResult
            if gameResult == 1:
                self.textResult = t.Text("Wygrał gracz pierwszy!",40,self.GREEN_COLOR)
            else:
                if gameResult == 2:
                    self.textResult = t.Text("Wygrał gracz drugi!",40,self.GREEN_COLOR)
                else:
                    if gameResult == 3:
                        self.textResult = t.Text("Remis",40,self.GREEN_COLOR)
                    else:
                        self.textResult = t.Text("Koniec gry",40,self.GREEN_COLOR)
#a = EndView(3)
#while True:
#    a.draw()
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            exit()