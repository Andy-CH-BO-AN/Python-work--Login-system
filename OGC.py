# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OGC.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorDialog(object):
    def setupUi(self, errorDialog):
        errorDialog.setObjectName("errorDialog")
        errorDialog.resize(459, 300)
        errorDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.horizontalLayout = QtWidgets.QHBoxLayout(errorDialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(errorDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)

        self.retranslateUi(errorDialog)
        QtCore.QMetaObject.connectSlotsByName(errorDialog)

    def retranslateUi(self, errorDialog):
        _translate = QtCore.QCoreApplication.translate
        errorDialog.setWindowTitle(_translate("errorDialog", "Dialog"))
        self.label.setText(_translate("errorDialog", "打手槍按ok"))
