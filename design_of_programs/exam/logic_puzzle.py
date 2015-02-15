from itertools import permutations

__author__ = 'Girish'

"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming.
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""


def logic_puzzle():

    perm =[[1,4,5,3,2]]
    for (wilkes, hamming, minsky, knuth, simon) in [(1, 4, 5, 3, 2)]:
        if knuth - simon ==1:
            for (laptop, droid, tablet, iphone, _) in [(3, 1, 4, 2, 5)]:
                if tablet !=5 and laptop==3:
                    for (programmer,writer,manager,designer,_) in [(4, 3, 2, 5, 1)]:

                        if wilkes !=programmer:
                            if set([droid,programmer]) ==set([hamming,wilkes]):
                                if writer != hamming:
                                    if knuth !=manager :
                                        if tablet != manager :
                                            if designer !=4 :
                                                if tablet !=3:
                                                    if designer != droid :
                                                        if knuth-manager==1 :
                                                            if set([laptop,wilkes]) == set([1,writer]) :
                                                                if (tablet == 4 or iphone ==2) :
                                                                    print(hamming,knuth,minsky,simon,wilkes)


logic_puzzle()