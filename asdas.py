import math

def sillycase(silly):
    bol =0
    if len(silly) &1 :
        bol=1
    strup = silly[:(len(silly)>>1)+bol]
    strdown =silly[(len(silly)>>1)+bol:].upper()
    return strup+strdown
