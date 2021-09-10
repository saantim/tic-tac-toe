
class TicTacToeGame():
    def __init__(self):
        self.board = self._create_board()
        self.turn = 1

    def get_turn(self):
        return self.turn

    def get_board(self):
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
        line = self.complete_line()
        if not line: return 0
        x, y = line[0]
        return self.board[y][x]

    def is_over(self):
        return self.full_board() or self.winner()

    def next_turn(self):
        if self.turn == 1: self.turn = 2
        else: self.turn = 1
        
    def complete_line(self):
        for y in range(3):
            aux = self.board[y][0]
            if not aux: continue
            if all(list(map(lambda x: x == aux, self.board[y]))):
                return [(0, y), (1, y), (2, y)]
        for x in range(3):
            aux = self.board[0][x]
            if not aux: continue
            if self.board[1][x] == aux and self.board[2][x] == aux:
                return [(x, 0), (x, 1), (x ,2)]
        cent = self.board[1][1]
        if not cent: return None
        if cent == self.board[0][0] and cent == self.board[2][2]:
            return [(0,0), (1,1), (2,2)]
        if cent == self.board[0][2] and cent == self.board[2][0]:
            return [(0,2), (1,1), (2,0)]
        return None

    def make_mark(self, x, y):
        if x < 0 or x > 2: return False
        if y < 0 or y > 2: return False
        if self.board[y][x]: return False
        self.board[y][x] = self.turn
        self.next_turn()
        return True
    
    def __str__(self):
        for line in self.board: print(line)
        return f"Next turn: Player {self.turn}"


if __name__ == "__main__":
    game = TicTacToeGame()
    
    game.make_mark(0,1)
    game.make_mark(0,0)
    game.make_mark(1,2)
    game.make_mark(1,1)
    game.make_mark(0,2)
    game.make_mark(2,2)

    print("over", game.is_over())
    print(game.full_board())
    print("winer", game.winner())
    print(game.complete_line())
    print(game)








