__author__ = 'Girish'
import itertools
def floor_puzzle():
    possibility = itertools.permutations([1,2,3,4,5])

    for (Hopper,kay, liskov,Perlis,Ritchie) in possibility:
        if Hopper is not 5:
            if kay is not 1:
                if liskov is not 1 and liskov is not 5:
                    if Perlis >kay:
                        if abs(Ritchie-liskov) != 1:
                            if abs(liskov-kay) != 1:
                                print(Hopper,kay,liskov,Perlis,Ritchie)





floor_puzzle()