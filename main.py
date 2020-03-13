import os
from datetime import time

import self as self
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
import json

import sys

from OGC import Ui_errorDialog
from OGC2 import Ui_OGC2
from createaccount import Ui_createaccount
from editpassword import Ui_editpasswordWindow
from mainOGC import Ui_MainWindow
from menuOGC import Ui_MenuWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self)

        # self.statusBar().showMessage('TEST Again!!!')
        self.setWindowIcon(QtGui.QIcon('picture/winniethepool.jpg'))

        image = QtGui.QPixmap()
        image.load('picture/stock.jpg')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)
        # Hide Window Title
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.main_ui.retranslateUi(self)

        self.main_ui.actionbye.setShortcut('Ctrl+Q')
        self.main_ui.loginpushButton.setShortcut('Return')
        self.main_ui.actionbye.triggered.connect(app.exit)
        self.main_ui.actionbye.setIcon(QtGui.QIcon('picture/winniethepool.jpg'))
        # self.main_ui.loginpushButton.setIcon(QtGui.QIcon('picture/winniethepool.jpg'))
        # self.main_ui.createaccountpushButton.setIcon(QtGui.QIcon('picture/winniethepool.jpg'))

        self.setWindowTitle('stock in the game')
        self.user_id = None

        self.main_ui.loginpushButton.clicked.connect(self.loginEvent)
        self.main_ui.createaccountpushButton.clicked.connect(self.connect_createaccount)

    def loginEvent(self):
        self.user_id = self.main_ui.userlineEdit.text()
        # login_user = select * from usertable where ID = self.main_ui.userlineEdit.text()
        self.user_password = self.main_ui.passwordlineEdit.text()
        # if password_user == select pw from usertable where ID = self.main_ui.userlineEdit.text()

        try:

            with open(f'./user_id/{self.user_id}.json', 'r') as load_f:
                user_dict = json.loads(load_f.read())

            if str(self.user_id) == str(user_dict['user_id']) and str(self.user_password) == str(
                    user_dict['user_password']):
                self.connect_menuWindow()

            else:
                self.connect_errorDialog()
        except:
            self.connect_errorDialog()
        self.main_ui.loginpushButton.clicked.connect(self.main_ui.userlineEdit.clear)
        self.main_ui.loginpushButton.clicked.connect(self.main_ui.passwordlineEdit.clear)

    def connect_errorDialog(self):
        self.w = errorDialog()
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.errorDialog_ui.label.setText("帳號密碼錯誤")
        self.w.show()

    def connect_menuWindow(self):
        self.w = menuWindow(self.user_id)
        self.w.show()
        self.hide()

    def connect_createaccount(self):
        self.w = createaccount()

        self.w.show()
        self.hide()


class errorDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.errorDialog_ui = Ui_errorDialog()
        self.errorDialog_ui.setupUi(self)
        self.mainDialog()

    def mainDialog(self):
        self.setMaximumSize(400, 250)
        self.setWindowTitle('error')
        self.errorDialog_ui.label.setStyleSheet("color:white;"
                                                "font: 17pt \"微軟正黑體\";")
        self.setWindowIcon(QtGui.QIcon('picture/winniethepool.jpg'))
        image = QtGui.QPixmap()
        image.load('picture/warning.jpg')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)


class OGCDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.Ui_OGC2 = Ui_OGC2()
        self.Ui_OGC2.setupUi(self)
        self.mainDialog()

    def mainDialog(self):
        self.setMinimumSize(700, 467)
        self.setWindowIcon(QtGui.QIcon('picture/icon.png'))
        self.resize(700,467)
        image = QtGui.QPixmap()
        image.load('picture/serval.jpg')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)


class createaccount(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.main_ui = Ui_createaccount()
        self.main_ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('picture/icon.png'))

        image = QtGui.QPixmap()
        image.load('picture/stock.png')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)
        self.setWindowTitle('stock in the game')
        self.main_ui.confirmpushButton.clicked.connect(self.createEvent)
        self.main_ui.cancelpushButton.clicked.connect(self.connectmainWindow)

    def createEvent(self):
        os.listdir()
        user_id = self.main_ui.userlineEdit.text()

        user_password = self.main_ui.passwordlineEdit.text()
        user_password_confirm = self.main_ui.confirmpasswordlineEdit.text()
        if user_password_confirm != user_password:
            self.connect_errorDialog()

        elif f'{user_id}.json' in os.listdir("./user_id"):
            self.connect_errorDialog_same_id()
        elif len(user_id) > 0 and len(user_password) > 0:
            user_dict = {}
            user_dict.setdefault('user_id', user_id)
            user_dict.setdefault('user_password', user_password)
            with open(f'./user_id/{user_id}.json', 'w') as f:

                json.dump(user_dict, f)

            f.close()
            self.connectmainWindow()
        else:
            self.connect_errorDialog_length_mistake()

    def connect_errorDialog(self):
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.userlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.passwordlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.confirmpasswordlineEdit.clear)
        self.w = errorDialog()
        self.w.errorDialog_ui.label.setText("密碼與確認密碼不同")
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.show()

    def connect_errorDialog_same_id(self):
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.userlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.passwordlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.confirmpasswordlineEdit.clear)
        self.w = errorDialog()
        self.w.errorDialog_ui.label.setText("已經有此帳號")
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.show()

    def connect_errorDialog_length_mistake(self):
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.userlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.passwordlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.confirmpasswordlineEdit.clear)
        self.w = errorDialog()
        self.w.errorDialog_ui.label.setText("帳號密碼要輸入")
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.show()

    def connectmainWindow(self):
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.userlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.passwordlineEdit.clear)
        self.main_ui.confirmpushButton.clicked.connect(self.main_ui.confirmpasswordlineEdit.clear)
        self.w = MainWindow()
        self.w.show()
        self.hide()


class menuWindow(QMainWindow):
    def __init__(self, user_id):
        super(menuWindow, self).__init__()

        self.main_ui = Ui_MenuWindow()
        self.main_ui.setupUi(self)
        self.user_id = user_id
        self.setWindowIcon(QtGui.QIcon('picture/winniethepool.jpg'))
        self.main_ui.label.setStyleSheet("color:white;")
        image = QtGui.QPixmap()
        image.load('picture/wagyu.jpg')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)
        self.setWindowTitle('menu')
        self.main_ui.editpasswordpushButton.setShortcut('R')
        self.main_ui.logoutpushbutton.clicked.connect(self.connectMainWindow)
        self.main_ui.editpasswordpushButton.clicked.connect(self.connectEditWindow)
        # self.main_ui.label.setText("您好:廢物")
        # main = MainWindow()
        self.main_ui.label.setText("您好:" + str(user_id))

    def connectMainWindow(self):
        self.w = MainWindow()
        self.w.show()
        self.hide()

    def connectEditWindow(self):
        self.w = EditWindow(self.user_id)
        self.w.show()
        self.hide()


class EditWindow(QMainWindow):
    def __init__(self, user_id):
        # QMainWindow.__init__(self)
        super(EditWindow, self).__init__()
        self.user_id = user_id
        self.main_ui = Ui_editpasswordWindow()
        self.main_ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('picture/icon.png'))

        image = QtGui.QPixmap()
        image.load('picture/A350.jpg')
        image = image.scaled(self.width(), self.height())

        # Palette
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(image))
        self.setPalette(palette)
        self.setWindowTitle("the winter is comming")
        self.main_ui.confirmpushButton.setShortcut('Return')
        self.main_ui.cancelpushButton.clicked.connect(self.connect_menuWindow)
        self.main_ui.confirmpushButton.clicked.connect(self.editEvent)
        self.main_ui.userlineEdit.setText(user_id)

    def editEvent(self):

        user_password = self.main_ui.passwordlineEdit.text()
        user_password_confirm = self.main_ui.confirmpasswordlineEdit.text()
        if self.main_ui.userlineEdit.text() != str(self.user_id):
            self.connect_OGC()
        elif user_password != user_password_confirm:
            self.connect_errorDialog()
        elif len(user_password) > 0:
            user_dict = {}
            user_dict.setdefault('user_id', self.user_id)
            user_dict.setdefault('user_password', user_password)
            with open(f'./user_id/{self.user_id}.json', 'w') as f:

                json.dump(user_dict, f)

            f.close()
            self.connect_menuWindow_edit_success()
        else:
            self.connect_errorDialog_length_mistake()

    def connect_menuWindow_edit_success(self):
        self.d = OGCDialog()
        self.d.setWindowTitle('success')
        self.d.Ui_OGC2.label.setText("修改成功")
        self.d.setGeometry(QRect(100, 100, 700, 467))
        self.d.Ui_OGC2.label.setStyleSheet("font: 48pt \"微軟正黑體\";color:white;")
        self.d.Ui_OGC2.buttonBox.setStyleSheet("font: 28pt \"微軟正黑體\";color:white;"
                                               "background-color:rgba(255, 255, 255, 120)")

        self.w = menuWindow(self.user_id)
        self.w.show()
        self.d.show()
        self.hide()

    def connect_errorDialog_length_mistake(self):
        self.w = errorDialog()
        self.w.errorDialog_ui.label.setText("密碼要輸入")
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.show()

    def connect_errorDialog(self):
        self.w = errorDialog()
        self.w.errorDialog_ui.label.setText("密碼與確認密碼不同")
        self.w.setGeometry(QRect(100, 100, 450,250))
        self.w.show()

    def connect_menuWindow(self):
        self.w = menuWindow(self.user_id)
        self.w.show()
        self.hide()

    def connect_OGC(self):

        self.w = OGCDialog()
        self.w.Ui_OGC2.label.setText('你他媽可以不要亂改帳號嗎?')
        self.w.setGeometry(QRect(100, 100, 700, 467))
        self.w.Ui_OGC2.label.setStyleSheet("font: 30pt \"微軟正黑體\";color:white;")
        self.w.Ui_OGC2.buttonBox.setStyleSheet("font: 28pt \"微軟正黑體\";color:white;"
                                               "background-color:rgba(255, 255, 255, 120)")
        self.w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    # 顯示

    window.show()
    sys.exit(app.exec_())
