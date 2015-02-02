# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watch.ui'
#
# Created: Mon Feb  2 09:46:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(354, 93)
        self.second = QtGui.QLCDNumber(Dialog)
        self.second.setGeometry(QtCore.QRect(270, 0, 81, 91))
        self.second.setAutoFillBackground(False)
        self.second.setFrameShape(QtGui.QFrame.Box)
        self.second.setSmallDecimalPoint(False)
        self.second.setNumDigits(2)
        self.second.setDigitCount(2)
        self.second.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.second.setProperty("value", 0.0)
        self.second.setObjectName(_fromUtf8("second"))
        self.sep2 = QtGui.QLabel(Dialog)
        self.sep2.setEnabled(True)
        self.sep2.setGeometry(QtCore.QRect(250, 0, 16, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sep2.setFont(font)
        self.sep2.setObjectName(_fromUtf8("sep2"))
        self.minute = QtGui.QLCDNumber(Dialog)
        self.minute.setGeometry(QtCore.QRect(160, 0, 81, 91))
        self.minute.setAutoFillBackground(False)
        self.minute.setFrameShape(QtGui.QFrame.Box)
        self.minute.setSmallDecimalPoint(False)
        self.minute.setNumDigits(2)
        self.minute.setDigitCount(2)
        self.minute.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.minute.setProperty("value", 0.0)
        self.minute.setProperty("intValue", 0)
        self.minute.setObjectName(_fromUtf8("minute"))
        self.sep = QtGui.QLabel(Dialog)
        self.sep.setGeometry(QtCore.QRect(140, 0, 16, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sep.setFont(font)
        self.sep.setObjectName(_fromUtf8("sep"))
        self.hour = QtGui.QLCDNumber(Dialog)
        self.hour.setGeometry(QtCore.QRect(50, 0, 81, 91))
        self.hour.setAutoFillBackground(False)
        self.hour.setFrameShape(QtGui.QFrame.Box)
        self.hour.setSmallDecimalPoint(False)
        self.hour.setNumDigits(2)
        self.hour.setDigitCount(2)
        self.hour.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.hour.setProperty("value", 0.0)
        self.hour.setProperty("intValue", 0)
        self.hour.setObjectName(_fromUtf8("hour"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.sep2.setText(_translate("Dialog", ":", None))
        self.sep.setText(_translate("Dialog", ":", None))

