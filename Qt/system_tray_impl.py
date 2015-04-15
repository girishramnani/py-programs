from PyQt4.QtCore import QTimer

__author__ = 'Girish'
import shelve
from PyQt4.QtGui import QIcon, QSystemTrayIcon, QApplication

__author__ = 'girish'
import requests
from bs4 import BeautifulSoup as Soup

import os
import sys

class Message_display:
    def __init__(self):
        self.t =QApplication(sys.argv)
        icon = QIcon("jBli3.png")
        self.tray = QSystemTrayIcon(icon)
        

        self.tray.show()


    def show_message(self,notification):
        assert type(notification) == Notification
        self.tray.showMessage(notification["title"],notification["body"])



    def exec_(self):
        self.t.exec_()

class Notification:
    def __init__(self,title,body):
        self.title=title
        self.body = body

    def __getitem__(self, item):
        return getattr(self,item)

name =Notification("girish","ramani")
message = Message_display()
message.show_message(name)
message.exec_()
