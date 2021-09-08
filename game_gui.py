import tkinter as tk
from tkinter import Place, messagebox
import game as g


class TicTacToeGui(tk.Frame):

    def __init__(self, root, game):
        tk.Frame.__init__(self, root)
        self.parent = root
        self.game = game[0]
        self.turn = game[1]
        self.config(width= 800, height= 600, bg="blue")

        self.canvas = tk.Canvas(self, width= 750, height= 550, bg="green")
        self.canvas.pack()
        
        turn = tk.Label(text=f"Now is Player {self.turn} turn!")
        turn.pack()

    def draw_pieces(self):
        o_posx = 0
        o_posy = 0
        
        pass




def design_table(game):
    frame_1 = tk.Frame()
    current_turn = tk.Label(text=f"Now is Player {game[1]} turn!")
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
    
    game = g.create_game()

    gui = TicTacToeGui(root, game)
    gui.pack(side= "top", fill= "both", expand="True")


    
    root.resizable(0,0)
    root.mainloop()


