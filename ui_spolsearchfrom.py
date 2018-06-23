# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_spolsearchform.ui'
#
# Created: Sat Jun 23 13:29:11 2018
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_SpolSearchForm(object):
    def setupUi(self, SpolSearchForm):
        SpolSearchForm.setObjectName(_fromUtf8("SpolSearchForm"))
        SpolSearchForm.resize(272, 193)
        self.gridLayout_2 = QtGui.QGridLayout(SpolSearchForm)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbLineEdit = QtGui.QLineEdit(SpolSearchForm)
        self.cbLineEdit.setObjectName(_fromUtf8("cbLineEdit"))
        self.gridLayout_2.addWidget(self.cbLineEdit, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(SpolSearchForm)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.kuLineEdit = QtGui.QLineEdit(SpolSearchForm)
        self.kuLineEdit.setObjectName(_fromUtf8("kuLineEdit"))
        self.gridLayout_2.addWidget(self.kuLineEdit, 0, 1, 1, 1)
        self.zpmzLineEdit = QtGui.QLineEdit(SpolSearchForm)
        self.zpmzLineEdit.setObjectName(_fromUtf8("zpmzLineEdit"))
        self.gridLayout_2.addWidget(self.zpmzLineEdit, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(SpolSearchForm)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(SpolSearchForm)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 0, 1, 1)

        self.retranslateUi(SpolSearchForm)
        QtCore.QMetaObject.connectSlotsByName(SpolSearchForm)

    def retranslateUi(self, SpolSearchForm):
        SpolSearchForm.setWindowTitle(_translate("SpolSearchForm", "Form", None))
        self.label_3.setText(_translate("SpolSearchForm", "KU", None))
        self.label_4.setText(_translate("SpolSearchForm", "ČB", None))
        self.label_2.setText(_translate("SpolSearchForm", "ZMPZ", None))

