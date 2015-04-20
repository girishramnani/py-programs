from time import strftime

__author__ = 'Girish'


from git import Repo
import glob
t = Repo("C:\\Users\\Girish\\Documents\\GitHub\\c_and_c++ Programs")
index = t.index
import os

import glob

import pytz

li=[diff.a_blob.path for diff in index.diff(None)]
for x in li:
    try:
        index.add([x])
    except FileNotFoundError:
        print(x)
        index.remove([x])



index.commit("synced at {}".format(strftime("%c")))
