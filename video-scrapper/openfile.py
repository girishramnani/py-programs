__author__ = 'girish'
file = open("E:\\1.tlog",'rb')
for x in file.readlines():
    print(x.decode())