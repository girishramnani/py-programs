
def choose_move(game_state):
    """Chooses a move to play given a game state"""
    nim_su =game_state[0]
    for i in game_state[1:]:
        nim_su ^=i
    li = list(filter(lambda x:x^nim_su < x ,game_state))
    return (game_state.index(li[0]),li[0]-(li[0]^nim_su))

print(choose_move([4,3,5]))
except
