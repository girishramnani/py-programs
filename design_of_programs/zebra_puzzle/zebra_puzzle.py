__author__ = 'Girish'

# for i in range(100, 999):
#     if i % 10 == (i // 10) % 10:
#         t = i * 2
#         if str(t)[0] == str(t)[2]:
#             print(i)
#
#
import string

tble = str.maketrans('ABC','123')
f = 'A+B==C'
print(eval(f.translate(tble)))

def valid(f):
    try:
        return eval(f)
    except ZeroDivisionError:
        return False
