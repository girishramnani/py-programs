from PyQt4.QtCore import Qt
from PyQt4.QtGui import QApplication, QMessageBox
from PyQt4.QtGui import QDialog
from PyQt4.QtGui import QLineEdit
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QPushButton
from PyQt4.QtGui import QVBoxLayout
from PyQt4.QtGui import QFileDialog

__author__ = 'Girish'
import sys
import urllib.request


class Py_downloader(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.Url = QLineEdit()
        self.save_location = QLineEdit()
        self.progress = QProgressBar()
        button = QPushButton("Download")
        browse = QPushButton("Browse")

        self.Url.setPlaceholderText("Enter the Url you wanna download")
        self.save_location.setPlaceholderText("Save file location")


        self.progress.setValue(0)
        self.progress.setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.Url)
        layout.addWidget(self.save_location)
        layout.addWidget(self.progress)
        layout.addWidget(browse)
        layout.addWidget(button)



        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()
        button.clicked.connect(self.download)
        browse.clicked.connect(self.show_dialog)

    def show_dialog(self):
        self.save_file = QFileDialog.getSaveFileName(self,caption="Save File as ",directory=".",filter="all files (*.*)")
        self.save_location.setText(self.save_file)


    def download(self):
        url = self.Url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self,"Warning","The download failed")
            self.reset()
            return

        QMessageBox.information(self, "Information", "The download is complete")
        self.reset()

    def reset(self):
        self.progress.setValue(0)
        self.Url.setText("")
        self.save_location.setText("")


    def report(self, blocknum, blocksize, totalsize):

        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = (readsofar * 100) / totalsize
            t = int(percent)
            print(t)
            self.progress.setValue(t)


app = QApplication(sys.argv)
main_window = Py_downloader()
main_window.show()
app.exec_()