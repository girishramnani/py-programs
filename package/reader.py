__author__ = 'Girish'

from package.compressed import gzipper


class reader:
    def __init__(self,filename):
        self.filename = filename
        self.f = open(self.filename,'rt')
    def close(self):
        self.f.close()
    def read(self):
        return self.f.read()
