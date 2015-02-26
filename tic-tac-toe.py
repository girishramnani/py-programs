__author__ = 'Girish'


board =[[None for x in range(3)] for x in range(3)]
board[0][0] ="O"
board[0][1] ="O"
board[0][2] ="O"



def check(board):
    def draw(board):
        for x in board:
            for y in x:
                if y ==None:
                    return False
        return True
    if (draw(board)):
        return True,None
    for x in range(len(board)):
        if board[x][0]==board[x][1]==board[x][2] != None:
            return True ,board[x][0]
        if board[0][x]==board[1][x]==board[2][x] != None:
            return True ,board[0][x]
    if board[0][0]==board[1][1]==board[2][2] !=None:
        return True ,board[0][0]
    if board[0][2]==board[1][1]==board[2][0] !=None:
        return True ,board[0][2]
    return False,None
play = True
def display(board):
    for x  in board:
        for i in x:
            print(i,end=" ")
        print()


while not check(board)[0]:

    choice =input("Enter Player 1 :" if play else "Enter Player 2 :")
    choice = list(map(int,choice.split(" ")))
    board[choice[0]][choice[1]] = "O" if play else "X"
    display(board)
    play = not play





