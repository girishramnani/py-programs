di ={'a':[5,5],'b':[7,2],'c':[5,0],'d':[4,6],'e':[7,7],'f':[5,2]}



li = sorted(di.keys(),key=lambda x:(2*di[x][1])/(di[x][0]*(di[x][0]-1)))

for x in di.keys():

    print(x,(2*di[x][1])/(di[x][0]*(di[x][0]-1)))
print(li)
