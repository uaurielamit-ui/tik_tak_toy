import sistem as s
def main():
    print("         ====start game=====")
    game_over = False
    while not game_over:
        scrine(d)
        s.x_move(d)
        chek_w=s.if_win(d, "x")
        if chek_w != None:
            scrine(d)
            print(chek_w)
            game_over = True
            break
        scrine(d)
        s.o_move(d)
        chek_w = s.if_win(d, "o")
        if chek_w != None:
            scrine(d)
            print(chek_w)
            game_over = True
            break






def  scrine(d):
    n_d=[]
    for data in d:
        if data == None:
            n_d.append ("  ")
        else:
            n_d.append (data)
    print(f"""
        [1]{n_d[0]} | [2]{n_d[1]} | [3]{n_d[2]} 
        =======+=======+=======
        [4]{n_d[3]} | [5]{n_d[4]} | [6]{n_d[5]}
        =======+=======+=======
        [7]{n_d[6]} | [8]{n_d[7]} | [9]{n_d[8]}
        """)



d = [None, None, None, None, None, None, None, None, None]
if __name__=="__main__":
    main() 