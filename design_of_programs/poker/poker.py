__author__ = 'Girish'

def rank(hands):
    if hands==None:
        raise TypeError
    if len(hands) ==1:
        return hands[0]
    return max(hands,key=_hand_rank)

def _hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(rank) and flush(hand):
        return (8,max(ranks))
    elif kind(4, ranks):
        return (7,kind(4,ranks),kind(1,ranks))
    elif kind(3,ranks) and kind(2,ranks):
        return (6,kind(3,ranks),kind(2,ranks))
    elif straight(ranks):
        return (4,max(ranks))
    elif flush(ranks):
        return (5,sorted(ranks,reverse=True))
    elif kind(3,ranks):
        return (3,kind(3,ranks),ranks)
    elif kind(2,ranks) and pair2(ranks):
        return (2,kind(2,ranks),pair2(ranks),kind(1,ranks))
    elif kind(2,ranks):
        return (1,kind(2,ranks),sorted(ranks,reverse=True))
    else:
        return (0,sorted(ranks,reverse=True))


hand_dict = 0
def _hand_dict(ranks):
    global hand_dict
    if hand_dict==0:
        hand_dict =dict()
        for i in ranks:
            hand_dict[i] = hand_dict.get(i,0)+1
    return hand_dict







