# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createaccount.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createaccount(object):
    def setupUi(self, createaccount):
        createaccount.setObjectName("createaccount")
        createaccount.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(createaccount)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userlabel = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        self.userlabel.setFont(font)
        self.userlabel.setObjectName("userlabel")
        self.horizontalLayout.addWidget(self.userlabel)
        self.userlineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.userlineEdit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.userlineEdit.setFont(font)
        self.userlineEdit.setStyleSheet("border-radius:15px;")
        self.userlineEdit.setText("")
        self.userlineEdit.setObjectName("userlineEdit")
        self.horizontalLayout.addWidget(self.userlineEdit)
        self.verticalLayout_2.addWidget(self.widget_3, 0, QtCore.Qt.AlignHCenter)
        self.widget_4 = QtWidgets.QWidget(self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.passwordlabel = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        self.passwordlabel.setFont(font)
        self.passwordlabel.setObjectName("passwordlabel")
        self.horizontalLayout_2.addWidget(self.passwordlabel)
        self.passwordlineEdit = QtWidgets.QLineEdit(self.widget_4)
        self.passwordlineEdit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.passwordlineEdit.setFont(font)
        self.passwordlineEdit.setStyleSheet("border-radius:15px;")
        self.passwordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordlineEdit.setObjectName("passwordlineEdit")
        self.horizontalLayout_2.addWidget(self.passwordlineEdit)
        self.verticalLayout_2.addWidget(self.widget_4, 0, QtCore.Qt.AlignHCenter)
        self.widget = QtWidgets.QWidget(self.widget_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 82, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.confirmpasswordlabel = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        self.confirmpasswordlabel.setFont(font)
        self.confirmpasswordlabel.setObjectName("confirmpasswordlabel")
        self.horizontalLayout_3.addWidget(self.confirmpasswordlabel)
        self.confirmpasswordlineEdit = QtWidgets.QLineEdit(self.widget)
        self.confirmpasswordlineEdit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.confirmpasswordlineEdit.setFont(font)
        self.confirmpasswordlineEdit.setStyleSheet("border-radius:15px;")
        self.confirmpasswordlineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordlineEdit.setObjectName("confirmpasswordlineEdit")
        self.horizontalLayout_3.addWidget(self.confirmpasswordlineEdit)
        self.verticalLayout_2.addWidget(self.widget, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.confirmpushButton = QtWidgets.QPushButton(self.widget_5)
        self.confirmpushButton.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.confirmpushButton.setFont(font)
        self.confirmpushButton.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,100);\n"
"border-radius:15px;\n"
"font: 20pt;")
        self.confirmpushButton.setObjectName("confirmpushButton")
        self.verticalLayout_3.addWidget(self.confirmpushButton, 0, QtCore.Qt.AlignRight)
        self.cancelpushButton = QtWidgets.QPushButton(self.widget_5)
        self.cancelpushButton.setMinimumSize(QtCore.QSize(200, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancelpushButton.setFont(font)
        self.cancelpushButton.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255,100);\n"
"border-radius:15px;\n"
"font: 20pt;")
        self.cancelpushButton.setObjectName("cancelpushButton")
        self.verticalLayout_3.addWidget(self.cancelpushButton, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.widget_5)
        createaccount.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(createaccount)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        createaccount.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(createaccount)
        self.statusbar.setObjectName("statusbar")
        createaccount.setStatusBar(self.statusbar)

        self.retranslateUi(createaccount)
        QtCore.QMetaObject.connectSlotsByName(createaccount)

    def retranslateUi(self, createaccount):
        _translate = QtCore.QCoreApplication.translate
        createaccount.setWindowTitle(_translate("createaccount", "MainWindow"))
        self.userlabel.setText(_translate("createaccount", "<html><head/><body><p><span style=\" color:#ffffff;\">帳號:</span></p></body></html>"))
        self.passwordlabel.setText(_translate("createaccount", "<html><head/><body><p><span style=\" color:#ffffff;\">密碼:</span></p></body></html>"))
        self.confirmpasswordlabel.setText(_translate("createaccount", "<html><head/><body><p><span style=\" color:#ffffff;\">確認密碼:</span></p></body></html>"))
        self.confirmpushButton.setText(_translate("createaccount", "確認"))
        self.cancelpushButton.setText(_translate("createaccount", "取消"))
