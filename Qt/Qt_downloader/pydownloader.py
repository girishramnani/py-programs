from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QVBoxLayout

__author__ = 'Girish'
import sys
import urllib.request


class Py_downloader(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()



        self.Url = QLineEdit()
        self.save_location  = QLineEdit()
        self.progress = QProgressBar()
        button  = QPushButton("Download")

        self.Url.setPlaceholderText("Enter the Url you wanna download")
        self.save_location.setPlaceholderText("Save file location")

        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.Url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(button)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()
        button.clicked.connect(self.download)

    def download(self):
        url = self.Url.text()
        save_location = self.save_location.text()
        urllib.request.urlretrieve(url,save_location,self.report)

    def report(self,blocknum,blocksize,totalsize):
        readsofar = blocknum*blocksize
        if totalsize >0:
            percent = readsofar *100 / totalsize
            self.progress.setValue(int(percent))
        
            


app = QApplication(sys.argv)
main_window = Py_downloader()
main_window.show()
app.exec_()