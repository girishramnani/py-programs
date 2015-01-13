__author__ = 'girish'
import os

def copy_file(file_from,to_file):
    readfile=open(file_from,'rb')
    writefile = open(to_file,'wb')
    while True:
        chunk = readfile.read(1024)
        if not chunk:
            break
        writefile.write(chunk)

copy_file("dbfile","tt")


def copy_dir(from_dir,to_dir):
    if not os.path.exists(os.path.abspath(to_dir)):
        os.mkdir(os.path.abspath(to_dir))
    for z in os.listdir(from_dir):
        file_name = os.path.join(from_dir,z)
        opfile = os.path.join(to_dir,z)
        if not os.path.isdir(file_name):

            copy_file(file_name,opfile)
            print('copying file from {} to {}'.format(file_name,opfile))
        else:
            copy_dir(file_name,opfile)

copy_dir("E:\mainSite","sf")

