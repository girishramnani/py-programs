from datetime import time
from itertools import permutations
from design_of_programs.crossword.func import timer

__author__ = 'Girish'
import time


def readwordlist(filename):
    file =set(open(filename).read().upper().split())
    ans = set(p for word in file for p in prefixes(word))
    return file,ans

@timer
def find_hand(hands,board_letters=None):
    if board_letters==None:
        hands = hands.upper()
    else:
        hands+=board_letters
    results=set()
    for i in range(1,len(hands)+1):
        for word in permutations(hands,i):
            word="".join(word)
            if word in WORD:
                results.add(word)
    return results
def prefixes(word):
    return [word[:i] for i in range(len(word))]



@timer
def find_words(letters,words=None):
    result=set()
    if words==None:
        words=""

    def extend_prefix(w,letters):
        if w in WORD: result.add(w)
        if w not in PREFIX :return
        for Li in range(len(letters)):
            L = letters[Li]

            extend_prefix(w+L,letters[:Li]+letters[Li+1:])
    extend_prefix('',letters+words)
    return result


def premutation(letters):
    result=set()
    t = len(letters)

    def worker(w,letters):

        if len(w)==t:

            result.add(w)

        for L in range(len(letters)):

            le = letters[L]
            worker(w+le,letters[:L]+letters[L+1:])


    worker("",letters)
    return result

print(premutation("ABCD"))
WORD,PREFIX = readwordlist("words.txt")
LETTER_POINTS =dict(A=1,B=3,C=3,D=2,E=1,F=4,G=2,H=4,I=1,J=8
                    ,K=5,L=1,M=3,N=1,O=1,P=3,Q=10,R=1,S=1,T=1,U=1,V=4,
                    W=4,X=8,Y=4,Z=10,_=0)

def word_score(word):
    return sum(LETTER_POINTS[x] for x in word)

def topn(hand,board_letters,n=10):
    words =find_words(hand,board_letters)
    li = sorted(words,key=word_score,reverse=True)
    return li[:n]

print(topn("LETTERS",None))

def longest_words(hand,board_letters=None):
    words = find_words(hand,board_letters)
    return sorted(words,key=len,reverse=True)


class anchor(set):pass

LETTERS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

ANY = anchor(LETTERS)
mnx= anchor('MNX')
moab=anchor('MOAB')
a_row = ['|','A',mnx,moab,'.','.',ANY,'B','E',ANY,'C',ANY,'.',ANY,'D',ANY,'|']
a_hand = 'ABCEHKN'
def row_plays(hand,row):
    result=set()


def legal_prefix(i,row):
    ans=""
    maxl=0
    for w in range(i-1,0,-1):
        if isinstance(row[w],anchor):
            break
        if row[w]=='.':
            ans+=" "
            maxl+=1
        else:
            ans+=row[w]
            maxl+=1
    return "".join(reversed(ans)),maxl

print(legal_prefix(2,a_row))





print(longest_words("LETTERS"))


def test2():
    print(find_words("LETTERS"))
    print(find_hand("LETTERS"))
    print(find_hand("ADEQUAT", 'IRE'))
    print(find_words("ADEQUAT", 'IRE'))

def test():
    global t
    t = time.time()
    print(find_hand("ABECEDR"))
    print(find_hand("AEINRST"))
    print(find_hand("DRAMITC"))
    print(find_hand("ADEINRST"))
    print(find_hand("TOXENSI"))
    print(find_hand(""))
    print(time.time() - t)

