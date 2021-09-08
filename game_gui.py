import tkinter as tk
import game


class TicTacToeGui(tk.Frame):

    def __init__(self, root, game):
        tk.Frame.__init__(self, root)
        self.parent = root
        self.game = game
        self.cell_size = 150

        self.config(width= 800, height= 600, bg="blue")
        self.canvas = tk.Canvas(self, width= 550, height= 550, bg="green")
        self.canvas.pack()
        turn = tk.Label(text=f"Now is Player {self.game.get_turn()}'s turn!")
        turn.pack()

    def draw_cells(self):
        board = self.game.get_board()
        for l in range(len(board)):
            for c in range(len(board[0])):
                self.draw_empty_cell(c, l)
                if board[l][c] == 1: self.draw_x(c, l)
                if board[l][c] == 2: self.draw_o(c, l)

    def draw_empty_cell(self, x_board, y_board):
        x0 = y0 = 50
        x1 = y1 = 200
        self.canvas.create_rectangle(
            x0 + (x_board * self.cell_size),
            y0 + (y_board * self.cell_size),
            x1 + (x_board * self.cell_size),
            y1 + (y_board * self.cell_size),
            fill="blue")

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

    def map_click(self):
        pass


def design_table(game):
    frame_1 = tk.Frame()
    current_turn = tk.Label(text=f"Now is Player {game[1]}'s turn!")
    current_turn.config(bg= "pink")
    
    current_turn.pack()
    frame_1.config(width=550, height=550)
    frame_1.pack()

    return frame_1

def show_cells(game):

    pass

def detectar_mouse(root):
    canvas = tk.Canvas(root, width = 100, height= 100)
    canvas.bind("<Button-1>", callback)
    canvas.pack()

def callback(event):
    print(f"clicked at {event.x}, {event.y}")
    mensaje = f"clicked at {event.x}, {event.y}"

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    
    tictactoe = game.TicTacToeGame()

    gui = TicTacToeGui(root, tictactoe)
    gui.pack(side= "top", fill= "both", expand="True")

    tictactoe.make_mark(1,1)
    tictactoe.make_mark(1,1)
    tictactoe.make_mark(1,2)
    gui.draw_cells()

    #root.resizable(0,0)
    root.mainloop()


