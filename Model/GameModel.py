class GameModel:
    def __init__(self):
        self.init()
    def init(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.firstPlayerTurn = True

    def insertSign(self,coordinates):
        if coordinates[0]<0 or coordinates[1]<0:
            return
        #need chceck if cord is int and in range
        if(self.board[coordinates[0]][coordinates[1]] == 0):
            self.board[coordinates[0]][coordinates[1]] = 1 if self.firstPlayerTurn else 2
            self.firstPlayerTurn = not(self.firstPlayerTurn)
        #checkingresult?
    def checkIfWin(self):
        column = True
        row = True
        for player in range(1,3):
            slant = True
            slant2 = True
            for i in range(0,len(self.board[0])):
                for j in range(0,len(self.board)):
                    if(self.board[i][j]!=player):
                        row = False
                    if(self.board[j][i]!=player):
                        column = False
                    if(self.board[i][i]!=player):
                        slant = False
                    if(self.board[len(self.board[0])-1-i][i]!= player):
                        slant2 =False
                if(column or row):
                    return True
                column = True
                row = True
            if(slant or slant2):
                return True
        return False

    def checkIfDraw(self):
        for i in range (0,3):
            if 0 in self.board[i]:
                return False
        if(self.checkIfWin()==False):
            return True
    def getResult(self):
        #0 - still playing
        #1 - win player 1
        #2 - win player 2
        #3 - draw
        if(self.checkIfWin()):
            if(self.firstPlayerTurn):
                return 2
            return 1
        if(self.checkIfDraw()):
            return 3
        return 0

    def ifFirstPlayerTurn(self):
        return self.firstPlayerTurn
    def getBoard(self):
        return self.board


