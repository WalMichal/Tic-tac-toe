import pygame
from View import Text as t
from View import Board as b
from View import Sign as s
from View import Window as w
class StartView(w.Window):
    def __init__(self,boardArray,boardPath,signsPaths):
        #dziedziczonko
        w.Window.__init__(self)
        #self.textPlayerTurn = Text("Ruch gracza ",30,self.GREEN_COLOR)
        self.textPlayer1 =t.Text("Ruch gracza pierwszego:",30,self.GREEN_COLOR)
        self.textSign1 = t.Text("O",30,self.BLACK_COLOR)
        self.textPlayer2 = t.Text("Ruch gracza drugiego:", 30, self.GREEN_COLOR)
        self.textSign2 = t.Text("X",30,self.BLACK_COLOR)
        self.textFirstWidth =self.textPlayer1.getLength()+self.textSign1.getLength()
        self.textSecondWidth =self.textPlayer2.getLength()+self.textSign2.getLength()
        self.P1Turn = True

        self.board = b.Board(boardArray, boardPath, self.boardCoordinates)
        self.nought = s.Sign(signsPaths[0])
        self.cross = s.Sign(signsPaths[1])

    def draw(self):
        super(StartView,self).draw()
        self.board.draw(self.screen,(self.nought, self.cross))
        if(self.P1Turn):
            self.textPlayer1.draw(self.screen,(self.RESOLUTION[1]/2-self.textFirstWidth/2,80))
            self.textSign1.draw(self.screen,(self.RESOLUTION[1]/2+self.textPlayer1.getLength()/2,80))
        else:
            self.textPlayer2.draw(self.screen, (self.RESOLUTION[1] / 2 - self.textSecondWidth/2, 80))
            self.textSign2.draw(self.screen, (self.RESOLUTION[1] / 2 + self.textPlayer2.getLength()/2, 80))
        pygame.display.flip()
    def getFieldCoordinates(self, coordinates):#?? wut
        return self.board.getFieldCoordinates(coordinates)
    def updatePlayerTurn(self,P1Turn):
        self.P1Turn = P1Turn
class A():
    def __init__(self):
        self.zmienna = 10
    def setZmienna(self,nowa):
        self.zmienna = nowa
    def print(self):
        print(self.zmienna)
class B():
    def __init__(self,zmienna):
        self.zmiennab = zmienna
    def set(self,zmienna):
        self.zmiennab = 8
    def print(self):
        print(self.zmiennab)


