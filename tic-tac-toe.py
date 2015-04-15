from pprint import pprint

__author__ = 'Girish'

import sys

sys.setrecursionlimit(100000)
board =[[None for x in range(3)] for x in range(3)]



class Node:
    WIN =1
    LOSE =3
    DRAW =2
    def __init__(self,move=None):
        self.move=move
        self.condition =None
        self.childrens=None


def possible_moves(board):
    moves = []
    for i,x in enumerate(board):
        for j, y in enumerate(x):
            if(y ==None):
                moves.append((i,j))
    return moves


def make_move(move,bol):
    board[move[0]][move[1]] = 'X' if bol else 'O'


count=0

def undo_move(move,bol):
    board[move[0]][move[1]] = None


def generate_tree(tree,bol):
    result,winner =check()
    if result:
        return winner
    for i,move in enumerate(possible_moves(board)):
        make_move(move,bol)
        winner = generate_tree(tree,not bol)

        display(board)
        print()
        if winner:

            undo_move(move,bol)
            return winner
    return None


def cp(array):
    a2 =array.copy()
    a2[0][0]=5
ar=[[1,2,3],[7,8,9],[45,89]]
cp(ar)
print(ar)






def check():

    """
    :param board: [[]]
    :return: tuple (Game end boolean , player won)
    """
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




