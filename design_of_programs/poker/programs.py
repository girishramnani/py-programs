__author__ = 'Girish'

def get_ints():
    i=1
    while True:
        yield i
        yield -i
        i+=1

