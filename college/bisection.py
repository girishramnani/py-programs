__author__ = 'Girish'
import matplotlib.pyplot as plt
import math

def function(x):
    return x**10 -1
'''The expression would be kept in the list as [1,2,1] which will mean x^2 +(2*x)+1'''
#List_of_expressions = [int(x) for x in input("Enter the expression : ").split()]

def regula_falsi(f,low,high):
    li=[]
    for x in range(20):
        mid = ((low*f(high))-(high*f(low)))/(f(high)-f(low))
        li.append(mid)
        if f(mid)<0:
            high = mid
        elif f(mid)>0:
            low = mid
    return li
def bisection(f,low,high):
    li =[]
    for x in range(20):
        mid = (low+high)/2
        li.append(mid)
        if f(low)*f(mid)==0:
            return mid
        elif f(low)*f(mid)<0:
            high = mid
        elif f(low)*f(mid)>0:
            low = mid
    return li
def function2(x):
    return ((667.38/x)*(1-(math.exp(-0.146843*x))))-40


li1= regula_falsi(function2,12,16)
li2=bisection(function2,12,16)

plt.figure()
plt.plot(li1)


plt.show()



