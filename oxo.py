__author__ = 'Girish'
import os

game_name = 'oxo_game.dat'

def getpath():
    return os.getcwd()

def save_game(lis):
    location = os.path.join(getpath(),game_name)
    with open(game_name,"w") as f:
        t = "".join(lis)
        f.write(t)

def retrive_game():
    location = os.path.join(getpath(),game_name)
    with open(location) as f:
        t = f.read()
        return list(t)

print(retrive_game())
