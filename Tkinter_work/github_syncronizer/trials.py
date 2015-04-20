from time import strftime

__author__ = 'Girish'


from git import Repo
import glob
t = Repo("C:\\Users\\Girish\\PycharmProjects\\compititive_coding")
index = t.index
import os

import glob

import pytz
print(t.untracked_files)

li=[diff.a_blob.path for diff in index.diff(None)]
print(li)



