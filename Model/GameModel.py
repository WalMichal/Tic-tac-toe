class GameModel:
    def __init__(self):
        self.init()

    def init(self):
        # 0 - empty field
        # 1 - first player sign
        # 2 - second player sign
        self.__board = [[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]]
        self.__first_player_turn = True

    def insert_sign(self, coordinates):
        if coordinates[0] < 0 or coordinates[1] < 0:
            return
        if self.__board[coordinates[0]][coordinates[1]] == 0:
            self.__board[coordinates[0]][coordinates[1]] = 1 if self.__first_player_turn else 2
            self.__first_player_turn = not self.__first_player_turn


    def check_if_win(self):
        column = True
        row = True
        for player in range(1, 3):
            slant = True
            slant2 = True
            for i in range(0, len(self.__board[0])):
                for j in range(0, len(self.__board)):
                    if self.__board[i][j] != player:
                        row = False
                    if self.__board[j][i] != player:
                        column = False
                    if self.__board[i][i] != player:
                        slant = False
                    if self.__board[len(self.__board[0]) - 1 - i][i] != player:
                        slant2 = False
                if column or row:
                    return True
                column = True
                row = True
            if slant or slant2:
                return True
        return False

    def check_if_draw(self):
        for i in range(0, 3):
            if 0 in self.__board[i]:
                return False
        if self.check_if_win() == False:
            return True

    def get_result(self):
        # 0 - still playing
        # 1 - win player 1
        # 2 - win player 2
        # 3 - draw
        if self.check_if_win():
            if self.__first_player_turn:
                return 2
            return 1
        if self.check_if_draw():
            return 3
        return 0

    def if_first_player_turn(self):
        return self.__first_player_turn

    def get_board(self):
        return self.__board
