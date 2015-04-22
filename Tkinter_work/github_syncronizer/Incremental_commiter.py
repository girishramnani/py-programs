from time import ctime
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showwarning
from tkinter.ttk import Label, Entry, Button, Combobox

__author__ = 'Girish'

import Mainview
class Ui2(Mainview.UI):

    def __init__(self,master):
        Mainview.UI.__init__(self,master)


    def init_UI(self):
        self.label = Label(self.master, text="Directory: ")
        self.entry = Entry(self.master, state='disabled', width=30)
        self.button = Button(self.master, text="Select Directory", command=self.ask)
        self.button2 = Button(self.master, text="start commiting", command=self.github.incremental_commit)
        self.button2.config(state="disabled")

        self.label.grid(row=0, column=0, pady=(5, 5), padx=(10))
        self.entry.grid(row=0, column=1, pady=(5, 5), padx=(10))
        self.button.grid(row=0, column=2, pady=(5, 5), padx=(2))
        self.button2.grid(row=0, column=3, padx=(2, 5))




if __name__ == "__main__":
    root = Tk()
    root.title("github incremental_commiter")
    root.minsize(320, 100)
    application = Ui2(root)
    root.mainloop()
