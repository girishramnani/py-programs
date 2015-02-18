__author__ = 'Girish'

def factorial_polinomial(coef):
    ans =[]
    j=1
    while len(coef) >=2:
        for i in range(1,len(coef)-1):
            coef[i]+=(coef[i-1]*j)
        ans.append(coef[-1])
        del(coef[-1])
        j+=1
    ans+=coef
    return reversed(ans)
print(list(factorial_polinomial([1,-12,42,-30,9])))
