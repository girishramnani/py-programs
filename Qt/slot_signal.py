from PyQt4.QtGui import QDialog, QHBoxLayout, QSpinBox, QDial, QApplication

__author__ = 'Girish'

class Form(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        layout =QHBoxLayout()
        self.spin = QSpinBox()
        self.dial =QDial()
        self.dial.setNotchesVisible(True)


        layout.addWidget(self.dial)
        layout.addWidget(self.spin)

        self.setLayout(layout)
        self.dial.valueChanged.connect(self.spin.setValue)
        self.spin.valueChanged.connect(self.dial.setValue)
        self.setWindowTitle("signals")
import sys
app =QApplication(sys.argv)
fp = Form()
fp.show()
app.exec_()
