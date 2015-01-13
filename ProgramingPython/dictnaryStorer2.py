__author__ = 'girish'
import pickle
import glob
import shelve
db = shelve.open("people")
for z in db.items():
    print(z)

db.close()