from PyQt4.QtGui import QDialog, QApplication, QPushButton
import numpy
import sys
import os
sys.path.append(os.path.abspath("Qt"))
from frame import Ui_Dialog

__author__ = 'Girish'


class Frame(QDialog,Ui_Dialog):

    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(self)
        self.where = numpy.where
        self.setWindowTitle("BULB GAME")
        self.list_of_buttons =numpy.reshape([getattr(self,"pushButton_{:02d}".format(i)) for i in range(0,25)],(5,5))
        self.buttonGroup.buttonClicked.connect(self.bulb_glow)
        self.pushButton_2.clicked.connect(self.random(5))
        self.adders = [(0,1),(1,0),(0,-1),(-1,0)]

    def bulb_glow(self,button):
        self.li = list(self.where(self.list_of_buttons == button))
        self.li = [int(self.li[0][0]),int(self.li[1][0])]
        print(self.li)
        for x,y in self.adders:
            if not( self.li[0]+x >=5 or  self.li[0]+x < 0 or  self.li[1]+y >=5 or self.li[1]+y <0 ):
                self.list_of_buttons[self.li[0]+x][self.li[1]+y].toggle()


    def random(self,n):

        def func():
            self.reset()
            from numpy.random import random
            li=list(map(lambda x: int(x*n) ,random(n)))
            li2=list(map(lambda x: int(x*n) ,random(n)))
            for x in range(n):
                self.list_of_buttons[li[x]][li2[x]].toggle()
        return func

    def reset(self):
    	for i in self.list_of_buttons:
            for j in i:
                j.setChecked(False)


    def won(self):
        pass


import sys
app =QApplication(sys.argv)

w= Frame()
w.show()
app.exec_()

