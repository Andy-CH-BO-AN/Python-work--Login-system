from __future__ import annotations

import os
import sys
from pathlib import Path

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow

from error_dialog_ui import Ui_ErrorDialog
from info_dialog_ui import Ui_InfoDialog
from auth import AuthService, UserAlreadyExists, UserStore, ValidationError
from create_account_ui import Ui_CreateAccountWindow
from edit_password_ui import Ui_EditPasswordWindow
from login_window_ui import Ui_LoginWindow
from menu_window_ui import Ui_MenuWindow

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "picture"
DEFAULT_USER_DATA_DIR = BASE_DIR / "data" / "users"


def _asset(name: str) -> str:
    return str(ASSET_DIR / name)


def _apply_background(widget, image_name: str) -> None:
    image = QtGui.QPixmap(_asset(image_name))
    if image.isNull():
        return
    image = image.scaled(
        widget.size(),
        QtCore.Qt.KeepAspectRatioByExpanding,
        QtCore.Qt.SmoothTransformation,
    )
    palette = widget.palette()
    palette.setBrush(widget.backgroundRole(), QtGui.QBrush(image))
    widget.setPalette(palette)


class ErrorDialog(QDialog):
    def __init__(self, message: str):
        super().__init__()
        self.ui = Ui_ErrorDialog()
        self.ui.setupUi(self)
        self.setMaximumSize(400, 250)
        self.setWindowTitle("錯誤")
        self.setWindowIcon(QtGui.QIcon(_asset("winniethepool.jpg")))
        self.ui.label.setText(message)
        self.ui.label.setStyleSheet('color:white;font: 17pt "微軟正黑體";')
        _apply_background(self, "warning.jpg")


class InfoDialog(QDialog):
    def __init__(self, message: str, title: str = "完成"):
        super().__init__()
        self.ui = Ui_InfoDialog()
        self.ui.setupUi(self)
        self.setMinimumSize(700, 467)
        self.resize(700, 467)
        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(_asset("icon.png")))
        self.ui.label.setText(message)
        self.ui.label.setStyleSheet('font: 48pt "微軟正黑體";color:white;')
        self.ui.buttonBox.setStyleSheet(
            'font: 28pt "微軟正黑體";color:white;'
            "background-color:rgba(255, 255, 255, 120)"
        )
        _apply_background(self, "serval.jpg")


class AppWindow(QMainWindow):
    def __init__(self, auth: AuthService):
        super().__init__()
        self.auth = auth
        self._next_window = None
        self._dialog = None

    def _open(self, window: QMainWindow) -> None:
        self._next_window = window
        window.show()
        self.hide()

    def _show_error(self, message: str) -> None:
        self._dialog = ErrorDialog(message)
        self._dialog.setGeometry(QRect(100, 100, 450, 250))
        self._dialog.show()

    def _show_info(self, message: str, title: str = "完成") -> None:
        self._dialog = InfoDialog(message, title)
        self._dialog.setGeometry(QRect(100, 100, 700, 467))
        self._dialog.show()


class MainWindow(AppWindow):
    def __init__(self, auth: AuthService):
        super().__init__(auth)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Stock in the Game")
        self.setWindowIcon(QtGui.QIcon(_asset("winniethepool.jpg")))
        _apply_background(self, "stock.jpg")

        self.ui.actionbye.setShortcut("Ctrl+Q")
        self.ui.loginpushButton.setShortcut("Return")
        self.ui.actionbye.triggered.connect(QApplication.instance().quit)
        self.ui.loginpushButton.clicked.connect(self.login)
        self.ui.createaccountpushButton.clicked.connect(self.open_create_account)

    def login(self) -> None:
        user_id = self.ui.userlineEdit.text().strip()
        password = self.ui.passwordlineEdit.text()
        try:
            if self.auth.authenticate(user_id, password):
                self._open(MenuWindow(self.auth, user_id))
            else:
                self._show_error("帳號或密碼錯誤")
        finally:
            self.ui.userlineEdit.clear()
            self.ui.passwordlineEdit.clear()

    def open_create_account(self) -> None:
        self._open(CreateAccountWindow(self.auth))


class CreateAccountWindow(AppWindow):
    def __init__(self, auth: AuthService):
        super().__init__(auth)
        self.ui = Ui_CreateAccountWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("建立帳號")
        self.setWindowIcon(QtGui.QIcon(_asset("icon.png")))
        _apply_background(self, "stock.png")

        self.ui.confirmpushButton.clicked.connect(self.create_account)
        self.ui.cancelpushButton.clicked.connect(self.back_to_login)

    def create_account(self) -> None:
        try:
            self.auth.register(
                self.ui.userlineEdit.text(),
                self.ui.passwordlineEdit.text(),
                self.ui.confirmpasswordlineEdit.text(),
            )
        except (ValidationError, UserAlreadyExists) as exc:
            self._show_error(str(exc))
            return

        self._show_info("帳號建立成功")
        self._open(MainWindow(self.auth))

    def back_to_login(self) -> None:
        self._open(MainWindow(self.auth))


class MenuWindow(AppWindow):
    def __init__(self, auth: AuthService, user_id: str):
        super().__init__(auth)
        self.user_id = user_id
        self.ui = Ui_MenuWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Menu")
        self.setWindowIcon(QtGui.QIcon(_asset("winniethepool.jpg")))
        self.ui.label.setStyleSheet("color:white;")
        self.ui.label.setText(f"您好:{user_id}")
        _apply_background(self, "wagyu.jpg")

        self.ui.editpasswordpushButton.setShortcut("R")
        self.ui.logoutpushbutton.clicked.connect(self.logout)
        self.ui.editpasswordpushButton.clicked.connect(self.open_edit_password)

    def logout(self) -> None:
        self._open(MainWindow(self.auth))

    def open_edit_password(self) -> None:
        self._open(EditPasswordWindow(self.auth, self.user_id))


class EditPasswordWindow(AppWindow):
    def __init__(self, auth: AuthService, user_id: str):
        super().__init__(auth)
        self.user_id = user_id
        self.ui = Ui_EditPasswordWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("修改密碼")
        self.setWindowIcon(QtGui.QIcon(_asset("icon.png")))
        _apply_background(self, "A350.jpg")

        self.ui.userlineEdit.setText(user_id)
        self.ui.userlineEdit.setReadOnly(True)
        self.ui.confirmpushButton.setShortcut("Return")
        self.ui.cancelpushButton.clicked.connect(self.back_to_menu)
        self.ui.confirmpushButton.clicked.connect(self.change_password)

    def change_password(self) -> None:
        try:
            self.auth.change_password(
                self.user_id,
                self.ui.passwordlineEdit.text(),
                self.ui.confirmpasswordlineEdit.text(),
            )
        except ValidationError as exc:
            self._show_error(str(exc))
            return

        self._show_info("修改成功", "Success")
        self._open(MenuWindow(self.auth, self.user_id))

    def back_to_menu(self) -> None:
        self._open(MenuWindow(self.auth, self.user_id))


def build_auth_service() -> AuthService:
    configured = os.getenv("LOGIN_SYSTEM_DATA_DIR")
    data_dir = Path(configured).expanduser() if configured else DEFAULT_USER_DATA_DIR
    return AuthService(UserStore(data_dir))


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow(build_auth_service())
    window.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())
