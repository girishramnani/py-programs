__author__ = 'girish'

import subprocess
pipe = subprocess.Popen("type graph.py ",stdout=subprocess.PIPE,shell=True)
girish = pipe.stdout.readlines()
for i in girish:
    print(i.decode())