__author__ = 'girish'

import os
import pprint
directory = "C:/"
l = os.walk("C:/")
for (thisdir,folders, files) in l:
    print(thisdir)
