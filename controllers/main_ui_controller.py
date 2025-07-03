from PyQt5 import QtWidgets
from ui.accounting_ui import Account_MainWindow
from controllers.account_controller import AccountController

class MainController:
    def __init__(self, ui, main_window, session_id):
        self.ui = ui
        self.main_window = main_window
        self.session = session_id
        self.ui.accounts_button.clicked.connect(self.open_account_module)
        self.account_window = None

    def open_account_module(self):
        # Create a new QMainWindow instance
        self.account_window = QtWidgets.QMainWindow()
        self.account_ui = Account_MainWindow()
        self.account_ui.setupUi(self.account_window)
        self.account_controller = AccountController(self.account_ui, self.account_window, self.session)
        self.account_window.show()
