__author__ = 'girish'
d = {'bob':{'job':'analyist','name':'Bob Smith','Pay':20000}}
REC="END."
def StoreDb(database,DBFile='dbfile'):
    opend=open(DBFile,'w')
    for key in database:
        print(key ,file=opend)
        for (name , value) in database[key].items():
            print(name+ "=>"+repr(value),file=opend)
        print(REC,file=opend)
    print("FileEnd.",file=opend)

def getDB(DBfile):
    database={}
    fil=open(DBfile)
    li=[]
    for i in fil.readlines():
        li.append(i.strip())
    print(li)
    d = {}
    key=li[0]
    d[key]={}
    del(li[0])
    i=0
    toogle=False
    while i<len(li):

        if li[i]=='END.':
            toogle = True
            i+=1
            continue

        if toogle:
            key=li[i+1]
            d[key]=dict()
            i+=1
            toogle=False
        else:
            spli = li[i].split("=>")
            d[key][spli[0]]=spli[1]
            i+=1
    return d
print(getDB("dbfile"))

