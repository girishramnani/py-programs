__author__ = 'Girish'

import os
import re


class Lister(list):
    '''Creates a list from the file given and has a method to find based on the word received'''
    def __init__(self,location=None):
        if location is None:
            self.location = os.path.join(os.path.abspath('./filtered.txt'))
        else:
            self.location = location
        print()
        self.file = open(self.location)
        self.extend(self.file.read().split())


    def search(self,text):
        return filter(lambda a:a.startswith(text),self)



