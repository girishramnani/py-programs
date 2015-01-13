
__author__ = 'girish'


def more(text, line =15):
    index = 0
    lines = text.splitlines()
    while lines:
        for z in lines[index:index+line]:
            print(z)
        lines=lines[index+line:]
        t = input("More?")
        if t not in ['y','Y']:
            break
def zip(iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result =[]
        for it in iterators:
            at = next(it)
            result.append(at)
        yield tuple(result)

def getmodules():
    import sys
    print(sys.modules)

def grails():
    raise IndexError
import sys
import traceback
try:
    grails()
except IndexError:
    execinfo = sys.exc_info()
    print(execinfo)
