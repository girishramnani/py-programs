__author__ = 'Girish'

func = lambda f: lambda n1: 1 if n1 == 0 else n1 * f(f)(n1 - 1)
ans= func(func)(5)

print(ans)
