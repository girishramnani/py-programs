__author__ = 'girish'

import sys
'''arg parser for parameterised arguments'''
def parse(text =sys.argv ):
    temp = text
    d=dict()
    while temp:
        if temp[0][0]=='-':
            d[temp[0]]=temp[1]
            temp= temp[2:]
    return d


print(parse(['-i','info','-g','work']))