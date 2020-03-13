# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OGC2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OGC2(object):
    def setupUi(self, OGC2):
        OGC2.setObjectName("OGC2")
        OGC2.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(OGC2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(OGC2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.buttonBox = QtWidgets.QDialogButtonBox(OGC2)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)

        self.retranslateUi(OGC2)
        self.buttonBox.accepted.connect(OGC2.accept)
        self.buttonBox.rejected.connect(OGC2.reject)
        QtCore.QMetaObject.connectSlotsByName(OGC2)

    def retranslateUi(self, OGC2):
        _translate = QtCore.QCoreApplication.translate
        OGC2.setWindowTitle(_translate("OGC2", "Dialog"))
        self.label.setText(_translate("OGC2", "hello bitch"))
