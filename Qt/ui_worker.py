__author__ = 'Girish'
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import urllib.request
import helloui
class Work(QDialog,helloui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.Download)
    def clear(self):
    def Download(self):
        word =self.lineEdit.text()
        location = self.lineEdit_2.text()
        try:

            urllib.request.urlretrieve(word, location,self.reportHook)
        except ValueError :
            QMessageBox.warning(self,"No url","No URL specified")
        except ConnectionError:
            QMessageBox
    def reportHook(self,chunk_num,chunk_size,total_size):
        temp_var= chunk_num*chunk_size
        if total_size>0:
            val = (temp_var*100)//total_size
            self.progressBar.setValue(val)




app = QApplication(sys.argv)
helloWor = Work()
helloWor.show()
app.exec_()

