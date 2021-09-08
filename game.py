import random
from tkinter import Canvas

class TicTacToeGame():
    def __init__(self):
        self.board = self._create_board()
        self.turn = random.randrange(1,3)

    def _create_board():
        table = []
        for y in range(3):
            table.append([])
            for x in range(3):
                table[y].append(0)
        return table

    def game_is_over(self):
        for y in range(len(self.board)):
            for x in self.board[y]:
                if x == 0: return False 
        return True

    def winner(self):
        for line in self.board:
            aux = line[0]
            if all(list(map(lambda x: x == aux))): 
                if aux: return self.turn
        
        for col in range(len(self.board)):
            aux = self.board[col]
            if aux == self.board[1][col] and aux == self.board[2][col]:
                if aux: return self.turn
        
        cent = self.board[1][1]
        if cent:
            if cent == self.board[0][0] and cent == self.board[2][2]:
                return self.turn
            if cent == self.board[0][2] and cent == self.board[2][0]:
                return self.turn
        return 0

    def make_mark(self, x, y):
        if x < 0 or x > 2: return False
        if y < 0 or y > 2: return False
        self.board[y][x] = self.turn
        return True