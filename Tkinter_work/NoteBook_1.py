__author__ = 'Girish'
from tkinter import *
from tkinter import ttk
root = Tk()
notebook=ttk.Notebook(root)

frame1 = ttk.Frame(notebook,height=500,width=400)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text = 'One')
notebook.add(frame2, text = 'Two')

frame1.config(height=400,width=400)
notebook.pack()
root.mainloop()