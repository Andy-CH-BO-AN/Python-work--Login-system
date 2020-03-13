# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuOGC.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        MenuWindow.setObjectName("MenuWindow")
        MenuWindow.resize(842, 676)
        MenuWindow.setStyleSheet("font: 75 28pt \"微軟正黑體\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(MenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 500))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.virtualsystem_button = QtWidgets.QPushButton(self.widget)
        self.virtualsystem_button.setMinimumSize(QtCore.QSize(400, 60))
        self.virtualsystem_button.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(255, 0, 0,120);\n"
"color:rgb(255, 255, 255);")
        self.virtualsystem_button.setObjectName("virtualsystem_button")
        self.gridLayout.addWidget(self.virtualsystem_button, 1, 0, 1, 1)
        self.logoutpushbutton = QtWidgets.QPushButton(self.widget)
        self.logoutpushbutton.setMinimumSize(QtCore.QSize(400, 60))
        self.logoutpushbutton.setStyleSheet("background-color: rgb(0, 85, 127,120);\n"
"border-radius:15px;\n"
"color:rgb(255, 255, 255);")
        self.logoutpushbutton.setObjectName("logoutpushbutton")
        self.gridLayout.addWidget(self.logoutpushbutton, 2, 0, 1, 1)
        self.banksystem_button = QtWidgets.QPushButton(self.widget)
        self.banksystem_button.setMinimumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.banksystem_button.setFont(font)
        self.banksystem_button.setStyleSheet("border-radius:15px;\n"
"color:rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255,120);")
        self.banksystem_button.setObjectName("banksystem_button")
        self.gridLayout.addWidget(self.banksystem_button, 1, 1, 1, 1)
        self.editpasswordpushButton = QtWidgets.QPushButton(self.widget)
        self.editpasswordpushButton.setMinimumSize(QtCore.QSize(400, 60))
        self.editpasswordpushButton.setStyleSheet("border-radius:15px;\n"
"background-color: rgb(170, 170, 255,120);\n"
"color:rgb(255, 255, 255);")
        self.editpasswordpushButton.setObjectName("editpasswordpushButton")
        self.gridLayout.addWidget(self.editpasswordpushButton, 2, 1, 1, 1)
        self.verticalLayout.addWidget(self.widget)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MenuWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 842, 53))
        self.menubar.setObjectName("menubar")
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MenuWindow)
        self.statusbar.setObjectName("statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MenuWindow)

    def retranslateUi(self, MenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MenuWindow.setWindowTitle(_translate("MenuWindow", "MainWindow"))
        self.label.setText(_translate("MenuWindow", "您好:"))
        self.virtualsystem_button.setText(_translate("MenuWindow", "虛擬下單系統"))
        self.logoutpushbutton.setText(_translate("MenuWindow", "登出"))
        self.banksystem_button.setText(_translate("MenuWindow", "銀行下單系統"))
        self.editpasswordpushButton.setText(_translate("MenuWindow", "修改密碼"))
