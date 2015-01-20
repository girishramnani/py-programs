__author__ = 'Girish'

from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Frame(root)
frame.pack()

frame.config(width=100,height=200,relief=RIDGE)
ttk.Button(frame,text="girsh").grid()
frame.config(padding=(30,15))
root.mainloop()