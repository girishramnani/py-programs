from collections import namedtuple

__author__ = 'Girish'
State = namedtuple('State','p me you pending')
def hold(state):
    return State(0 if state.p else 1,state.you,state.me+state.pending,0)

def roll(state,d):
    if d==1:
        return State(0 if state.p else 1,state.you,state.me+1,0)
    else:
        return (state.p,state.me,state.you,state.pending+d)

import random

possible_moves = [' roll','head']

def clueless(state):
    return random.choice(possible_moves)

def hold_at(x):
    def strategy(state):
        (p,me,you,pending) =state
        return 'hold' if (pendo)



    strategy.__name__ ='hold_at(%d)' % x
    return strategy