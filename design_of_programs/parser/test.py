__author__ = 'Girish'
def alt(x,y):return lambda text:x(text) | y(text)


x=set(range(5))
y= set(range(6))
print(alt(x,y)("1234"))