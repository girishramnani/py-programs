
from tkinter import *

from threading import Thread
root =Tk()
label_li=[]
label =Label(text="hello")
label.pack(side=BOTTOM)
label_li.append(label)

label =Label(text="hello")
label.pack(side=TOP)
label_li.append(label)


label =Label(text="hello")
label.pack(side=RIGHT)
label_li.append(label)

label =Label(text="hello")
label.pack(side=LEFT)
label_li.append(label)
import time
def method():
	while True:
		for label in label_li:

			for pattern in ['--','\\','|','/']:
				time.sleep(0.1)
				label["text"]=pattern




Thread(target=lambda : method()).start()
root.mainloop()
