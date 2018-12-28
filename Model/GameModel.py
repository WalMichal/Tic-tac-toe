class GameModel:
    def __init__(self):
        self.init()
    def init(self):
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]
        self.firstPlayerTurn = True

    def insertSign(self,coordinates):
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
            for i in range(0,3):
                for j in range(0,3):
                    if(self.board[i][j]!=player):
                        row = False
                    if(self.board[j][i]!=player):
                        column = False
                    if(self.board[i][i]!=player):
                        slant = False
                if(column or row):
                    return True
                column = True
                row = True
            if(slant):
                return True
        return False
        #0 - no win
        #1 - win player 1
        #2 - win player 2
    def checkIfDraw(self):
        for i in range (0,3):
            if 0 in self.board[i]:
                return False
        if(self.checkIfWin()==False):
            return True

    def ifFirstPlayerTurn(self):
        return self.firstPlayerTurn
    def getBoard(self):
        return self.board

a = GameModel()
print(a.firstPlayerTurn)
#a.insertSign((0,1))
print(a.firstPlayerTurn)
print(a.checkIfWin())


