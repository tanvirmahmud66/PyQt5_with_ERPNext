# controllers/login_controller.py
from PyQt5.QtWidgets import QMessageBox
from services.login_api import LoginAPI
from PyQt5 import QtWidgets
import sys
from ui.main_ui import Ui_MainWindow
from controllers.main_ui_controller import MainController



class LoginController:
    def __init__(self, ui, login_window):
        self.ui = ui
        self.login_window = login_window
        self.api = LoginAPI("http://localhost:8000")  # set your Frappe URL here

        # connect the button click to login handler
        self.ui.login_button.clicked.connect(self.handle_login)

    def handle_login(self):
        username = self.ui.username_input.toPlainText().strip()
        password = self.ui.textEdit_2.toPlainText().strip()  # or change to password_input if renamed

        if not username or not password:
            QMessageBox.warning(self.login_window, "Input Error", "Please enter username and password")
            return

        result = self.api.login(username, password)
        if result["success"]:
            QMessageBox.information(self.login_window, "Success", "Login successful!")
            # Close login window and open main UI window
            self.session = result["session"]  # 🔁 store session
            self.sid = result["sid"]
            self.login_window.close()
            self.open_main_ui()
        else:
            QMessageBox.critical(self.login_window, "Login Failed", f"Login failed: {result.get('error')}")



    def open_main_ui(self):
        self.main_window = QtWidgets.QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self.main_window)
        self.main_controller = MainController(self.main_ui, self.main_window, self.sid)
        self.main_window.show()
