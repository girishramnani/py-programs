from functools import reduce
from numpy import *

class BinaryStream:
    def __init__(self, file=None, st=None):
        if file != None:
            print("trying to read as a file")
            self.reader = open(file, 'rb')
            self.IsFile = True
        elif st != None:
            print("using it as a String")
            self.reader = st
            self.IsFile = False

    def encode(self):
        li = []

        if self.IsFile:
            for i in self.reader.readlines():
                li.append([bin(x) for x in i])
            self.dataStream = [z for x in li for z in x]
        else:
            encoded = self.reader.encode()
            self.dataStream = [bin(z) for z in encoded]

        return self._convertToInt()


    def _mapWrapper(self):
        def apply(string):
            return ('0'*(8-len(string[2:])))+string[2:]
        return apply


    def _convertToInt(self):
        li = list(map(self._mapWrapper(),self.dataStream))
        self.binaryList=[int(y) for x in li for y in x]
        print(len(self.binaryList))
        print(li)
        return self.binaryList


bo = BinaryStream("giris")
print(bo.encode())
