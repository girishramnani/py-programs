__author__ = 'girish'
import glob
import os

def binary_file_joiner(pattern,tofile,lastchunk):
    file = open(tofile,'wb')
    for i in range(lastchunk+1):
        file.write(join(open(pattern+str(i),'rb').readlines()))

binary_file_joiner("part","sdf",58)