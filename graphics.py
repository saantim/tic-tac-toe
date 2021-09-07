import tkinter as tk

def create_window():
    root = tk.Tk()
    root.geometry("600x600")
    root.title("Tic-Tac-Toe")
    root.resizable(0,0)
    root.config(bg = "green")
    return root

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


def click_at(root):
    canvas = tk.Canvas(root, width = 100, height= 100)
    canvas.bind("<Button-1>", callback)
    canvas.pack()


def callback(event):
    print(f"clicked at {event.x}, {event.y}")