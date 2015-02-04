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
        t =QApplication(sys.argv)
        icon = QIcon("jBli3.png")
        self.tray = QSystemTrayIcon(icon)
        self.tray.show()
        t.exec_()
    def show_message(self,download):
        self.tray.showMessage("Downloading",download)

x =Message_display()

