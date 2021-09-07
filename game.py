import random
import graphics

def main():

    game = create_game()
    window = graphics.create_window() 
    graphics.design_table(game)
    graphics.click_at(window)

    window.mainloop()
    return

def gamer_is_over(game):
    for y in range(len(game[0])):
        for x in game[0][y]:
            if x == 0: return False 
    return complete_line(game)

def complete_line(game):
    table = game[0]
    for line in table:
        aux = line[0]
        if all(list(map(lambda x: x == aux))): return True
    for col in range(len(game[0])):
        aux = table[col]
        if aux == game[1][col] and aux == game[2][col]:
            return True
    cent = table[1][1]
    if cent == table[0][0] and cent == table[2][2]:
        return True
    if cent == table[0][2] and cent == table[2][0]:
        return True
    return False

def create_game():
    return (create_table(), random.randrange(1,3))

def create_table():
    table = []
    for y in range(3):
        table.append([])
        for x in range(3):
            table[y].append(0)
    return table


main()