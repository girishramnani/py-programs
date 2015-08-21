__author__ = 'Girish'



from tkinter import *

class TerminalHandler:
    def __init__(self,master):
        self.master = master
    def new_window(self,title=""):
        self.newWindow = Toplevel(self.master)
        self.newWindow.title(title)
        self.app = Terminal(self.newWindow)
        return self.app


class Terminal:
    def __init__(self, master):
        self.master = master
        self.scrollTxtArea = scrollTxtArea(self.master)

    def print(self,message):
        self.scrollTxtArea.text.insert(END,message+"\n")
        self.scrollTxtArea.text.yview(END)


class scrollTxtArea:
    def __init__(self,root):
        frame=Frame(root)
        frame.pack()
        self.textPad(frame)
        return

    def textPad(self,frame):
        textPad=Frame(frame)
        self.text=Text(textPad,height=20,width=120)
        # add a vertical scroll bar to the text area
        self.scroll=Scrollbar(textPad)
        self.text.configure(yscrollcommand=self.scroll.set)
        #pack everything
        self.text.pack(side=LEFT)
        self.scroll.pack(side=RIGHT,fill=Y)
        textPad.pack(side=TOP)
        return


