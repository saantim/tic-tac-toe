import random

class TicTacToeGame():
    def __init__(self):
        self.board = self._create_board()
        self.turn = 1

    def current_turn(self):
        return self.turn

    def current_board(self):
        return self.board

    def _create_board(self):
        table = []
        for y in range(3):
            table.append([])
            for x in range(3):
                table[y].append(0)
        return table

    def full_board(self):
        for y in range(len(self.board)):
            for x in self.board[y]:
                if x == 0: return False 
        return True

    def winner(self):
        #If there is a winner return his Player's number, otherwise returns 0
        for line in self.board:
            aux = line[0]
            if all(list(map(lambda x: x == aux, line))): 
                if aux: return aux
        for col in range(len(self.board)):
            aux = self.board[0][col]
            if aux == self.board[1][col] and aux == self.board[2][col]:
                if aux: return aux
        cent = self.board[1][1]
        if not cent: return 0
        if cent == self.board[0][0] and cent == self.board[2][2]:
            return aux
        if cent == self.board[0][2] and cent == self.board[2][0]:
            return aux
        return 0

    def is_over(self):
        return self.full_board() or self.winner()

    def make_mark(self, x, y):
        if x < 0 or x > 2: return False
        if y < 0 or y > 2: return False
        if self.board[y][x]: return False
        self.board[y][x] = self.turn
        if self.turn == 1: 
            self.turn = 2
        else: 
            self.turn = 1
        return True
    
    def __str__(self):
        for line in self.board: print(line)
        return f"Next turn: Player {self.turn}"


if __name__ == "__main__":
    game = TicTacToeGame()
    
    game.make_mark(0,1)
    game.make_mark(1,1)
    game.make_mark(0,0)
    game.make_mark(1,2)
    game.make_mark(0,2)

    print(game.is_over())
    print(game.full_board())
    print(game.winner())

    print(game)








