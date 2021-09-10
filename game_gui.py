import tkinter as tk
from tkinter.simpledialog import askstring
import tic_tac_toe


class TicTacToeGui(tk.Frame):

    def __init__(self, root, game):
        tk.Frame.__init__(self, root)
        self.parent = root
        self.game = game
        self.cell_size = 150
        self.current_turn = 0
        self.label_text = tk.StringVar()

        self.config(width= 800, height= 600, bg="blue")
        self.canvas = tk.Canvas(self, width= 550, height= 550, bg="green")
        self.canvas.pack()

        label_turn = tk.Label(textvariable= self.label_text, font=("Purisa", 25))
        label_turn.pack()

        self.canvas.bind("<Button-1>", self.click)
        self.draw_board()
        self.show_turn()
        
    def draw_board(self):
        board = self.game.get_board()
        for l in range(len(board)):
            for c in range(len(board[0])):
                self.draw_cell(c, l, "blue")
                if self.game.get_winner() and (c, l) in self.game.complete_line():
                    self.draw_cell(c, l, "red")
                if board[l][c] == 1: self.draw_x(c, l)
                if board[l][c] == 2: self.draw_o(c, l)

    def draw_cell(self, x_board, y_board, colour):
        x0 = y0 = 50
        x1 = y1 = 200
        self.canvas.create_rectangle(
            x0 + (x_board * self.cell_size),
            y0 + (y_board * self.cell_size),
            x1 + (x_board * self.cell_size),
            y1 + (y_board * self.cell_size),
            fill=colour)

    def draw_x(self, x_board, y_board):
        self.canvas.create_text(
            125 + (x_board * self.cell_size),
            130 + (y_board * self.cell_size),
            fill="pink", text="X", font=("Purisa", 150))

    def draw_o(self, x_board, y_board):
        self.canvas.create_text(
            125 + (x_board * self.cell_size),
            130 + (y_board * self.cell_size),
            fill="cyan", text="O", font=("Purisa", 150))

    def click(self, event):
        if self.game.is_over(): return
        x = event.x
        y = event.y

        x0 = y0 = 50
        x1 = y1 = 200
        board = self.game.get_board()
        for y_board in range(len(board)):
            for x_board in range(len(board[0])):
                cell_x0 = x0 + (x_board * self.cell_size)
                cell_x1 = x1 + (x_board * self.cell_size)
                cell_y0 = y0 + (y_board * self.cell_size)
                cell_y1 = y1 + (y_board * self.cell_size)
                if x > cell_x0 and x < cell_x1 and y > cell_y0 and y < cell_y1:
                    self.game.make_mark(x_board, y_board)
        self.draw_refresh()

    def show_turn(self):
        self.label_text.set(value=f"Now is Player {self.game.get_turn()}'s turn!")

    def show_winner(self):
        if not self.game.get_winner():
            self.label_text.set(value=f"It's a Draw!")    
        else:
            self.label_text.set(value=f"Player {self.game.get_turn()} wins!!!")

    def draw_refresh(self):
        self.draw_board()
        self.show_turn()
        if self.game.is_over():
            self.show_winner()

def display(game):
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    gui = TicTacToeGui(root, game)
    gui.pack(side= "top", fill= "both", expand="True")
    root.resizable(0,0)
    root.mainloop()
