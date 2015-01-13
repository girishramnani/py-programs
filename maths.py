__author__ = 'Girish'

def su(nu):
    count=0
    for x in range(1,(nu//2)+1):
        if nu%x==0:
            count+=x
    count+=nu
    return count

su2=0
for i in range(1,101):
    su2+=su(i)
print(su2)

