__author__ = 'Girish'

def rank(hands):
    if hands==None:
        raise TypeError
    if len(hands) ==1:
        return hands[0]
    return max(hands,key=_hand_rank)

def _hand_rank(hand):
    pass

