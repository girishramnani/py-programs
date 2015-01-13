__author__ = 'girish'

import os
def breaker(from_file,to_dir,chunk):
    if not os.path.isfile(from_file):
        raise FileNotFoundError
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    file = open(from_file,mode='rb')
    i=0
    while True:
        word = file.read(chunk)
        if not word:
            break
        filename = os.path.join(to_dir,"part{}".format(i))
        i+=1
        open(filename,'wb').write(word)




breaker("dbfile",'.',1)