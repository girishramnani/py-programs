__author__ = 'Girish'
from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self,master):
        self.label = ttk.Label(master,text="Hello, tkinter")
        self.label.grid(row=0,column = 0,columnspan=2)
        ttk.Button(master , text = "Texas",
                   command = self.texas_hello).grid(row=1,column=0)
        ttk.Button(master , text = "Hawaii",
                   command = self.hawai_hello).grid(row=1,column=1)


    def texas_hello(self):
        self.label.config(text="Howdi")
    def hawai_hello(self):
        self.label.config(text="Hehaha")
root = Tk()
app = HelloApp(root)
root.mainloop()