__author__ = 'girish'


dif = dict()
for z in range(1,10):
    dif[z]=1/z
print(sorted( dif.items(),key=lambda x:x[1]),)

