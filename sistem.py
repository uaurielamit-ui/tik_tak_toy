import val
import main
WINNING_LINES = [
(0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6),
]
def x_move(data):
    legal = False
    while not legal:
        x = val.get_int(" x its your torn enter your choice: ")-1
        if data[x] == None:
            legal = True
    data[x]="x"


def o_move(data):
    legal = False
    while not legal:
        o = val.get_int(" o its your torn enter your choice: ")-1
        if data[o] == None:
            legal = True
    data[o]="o"

def if_win(data, p):
    win = None
    for winning in WINNING_LINES:
        end = 0
        for w in winning:
            if data[w]== p:
                end += 1
        if end == 3:        
            win = f"{p} win!!!!!!"
            break
    if not None in data:
        if win == None:
            wim = f"aot of moves no winner this time "
            
    return win 



    
