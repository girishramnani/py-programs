from tkinter.ttk import Combobox

__author__ = 'Girish'
from tkinter import messagebox
from tkinter.messagebox import showwarning, showinfo
from tkinter.filedialog import askopenfilename, askdirectory
import os
from tkinter import *
import tkinter.ttk as ttk

# from . import Github_api


class UI:
    def __init__(self, master):
        # self.github = Github_api.Github()

        self.master = master
        self.init_UI()


    def init_UI(self):
        self.label = Label(self.master, text="Directory: ")
        self.entry = Entry(self.master, state='disabled', width=30)
        self.button = Button(self.master, text="Select Directory", command=self.ask)
        self.button2 = Button(self.master, text="startSync", command=self.start_syncronysing)
        self.button2.config(state="disabled")
        self.minlabel = Label(self.master, text="Every ..")
        self.min2label = Label(self.master, text=" minutes")
        self.combobox = Combobox(self.master, values=[1, 5, 30, 60])
        self.combobox.set(1)
        self.label.grid(row=0, column=0, pady=(5, 5), padx=(10))
        self.entry.grid(row=0, column=1, pady=(5, 5), padx=(10))
        self.button.grid(row=0, column=2, pady=(5, 5), padx=(2))
        self.button2.grid(row=0, column=3, padx=(2, 5))
        self.minlabel.grid(row=1, column=0, padx=(2, 5), pady=(5, 6))
        self.combobox.grid(row=1, column=1, padx=(2, 5), pady=(5, 6))
        self.min2label.grid(row=1, column=2, padx=(2, 5), pady=(5, 6), sticky="w")


    def ask(self):
        self.directory = askdirectory(title="Select the directory", mustexist=True)

        if self.directory:
            self.button2.config(state="normal")
            self.entry.config(state="normal")
            self.entry.delete(0)
            self.entry.insert(0, self.directory)
            self.entry.config(state="disabled")
            # self.github.setrepository(self.directory)
        else:
            showwarning("You didnt select any directory?")


    def start_syncronysing(self):
        pass
        # import time
        #     self.github.add_all()
        #     self.github.commit("sync at "+time.time())
        #     if self.remote:
        #         try:
        #             self.github.push()
        #             self.master.after(self.start_syncronysing,self.combobox.get()*60)
        #         except NoRemoteException:
        #             showinfo()


if __name__ == "__main__":
    root = Tk()
    root.title("github sycnroniser")
    root.minsize(320, 100)
    application = UI(root)
    root.mainloop()

