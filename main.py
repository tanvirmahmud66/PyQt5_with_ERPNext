


# main.py
import sys
from PyQt5 import QtWidgets
from ui.login_ui import LoginWindow
from controllers.login_controller import LoginController

def main():
    app = QtWidgets.QApplication(sys.argv)
    login_window = QtWidgets.QMainWindow()
    ui = LoginWindow()
    ui.setupUi(login_window)
    controller = LoginController(ui, login_window)
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
