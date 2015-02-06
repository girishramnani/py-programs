__author__ = 'Girish'
import random
def deal(numhands,n=5,deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:(n*(i+1))] for i in range(numhands)]


print(deal(6))
def rank(hands):
    if hands is None:
        raise TypeError
    if len(hands) == 1:
        return hands[0]
    return allmax(hands, key=_hand_rank)

def allmax(iterable,key=None):
    li=[iterable[0]]
    for x in iterable[1:]:
        if key(x) >key(li[0]):
            li=[x]
        elif key(x)==key(li[0]):
            li.append(x)
    return li[0] if len(li)==1 else li

def card_ranks(cards):
    card_mapping = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    ranks = [card_mapping.get(r, r) for r,s in cards]
    ranks = [int(x) for x in ranks]
    ranks.sort(reverse=True)

    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def reporduce(n=100000):
    dealno=dict()
    for i in range(n):
        x= deal(1)
        temp=_hand_rank(*x)
        dealno[temp[0]]=dealno.get(temp[0],0)+1
    for x,y in dealno.items():
        print("{} {} %".format(x,y*100/n))


def straight(card):
    t=list(range(card[0],card[0]-5,-1))
    if t ==card:
        return True
    return False

def flush(hand):
    cmp = hand[0][1]
    for r,s in hand:
        if cmp !=s:
            return False
    return True
def kind(no,ranks):
    occurrence_dict = _hand_dict(ranks)
    for j in occurrence_dict.keys():
        if occurrence_dict[j] ==no:
            return j
    return None

def _hand_dict(ranks):
    hand_dict=dict()
    for i in ranks:
        hand_dict[i] = hand_dict.get(i, 0) + 1
    return hand_dict

def two_pair(ranks):
    dt = _hand_dict(ranks)
    li=[]
    for z in dt.keys():
        if dt[z] ==2:
            li.append(z)
    if len(li) != 2:
        return None
    return sorted(li,reverse=True)

def _hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif straight(ranks):
        return (4, max(ranks))
    elif flush(hand):
        return (5, sorted(ranks, reverse=True))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), sorted(ranks, reverse=True))
    else:
        return (0, sorted(ranks, reverse=True))


reporduce()

