from PyQt5 import QtWidgets
from ui.journal_entry_ui import Ui_MainWindow as JournalEntryUI
from services.journal_entry_api import JournalEntryAPI

class AccountController:
    def __init__(self, ui, window, session_id):
        self.ui = ui
        self.window = window
        self.session_id = session_id

        # Assume 'journal_entry_button' exists on main UI and connects to open_journal_entry
        self.ui.journal_entry_button.clicked.connect(self.open_journal_entry)

    def open_journal_entry(self):
        self.journal_window = QtWidgets.QMainWindow()
        self.journal_ui = JournalEntryUI()
        self.journal_ui.setupUi(self.journal_window)

        self.journal_ui.doctype_label.setText("Journal Entry")

        self.populate_list()

        self.journal_window.show()

    def populate_list(self):
        api = JournalEntryAPI("http://localhost:8000", sid=self.session_id)
        result = api.get_journal_entries()

        if result["success"]:
            data = result["data"]

            self.journal_ui.listWidget.clear()

            for entry in data:
                # Format display string as you want
                name = entry.get("name", "")
                posting_date = entry.get("posting_date", "")
                voucher_type = entry.get("voucher_type", "")
                company = entry.get("company", "")
                total_debit_val = entry.get("total_debit", 0)

                try:
                    total_debit_str = f"৳ {float(total_debit_val):,.2f}"
                except (ValueError, TypeError):
                    total_debit_str = "৳ 0.00"

                display_text = (f"{name} | Date: {posting_date} | Voucher: {voucher_type} | "
                                f"Company: {company} | Debit: {total_debit_str}")

                self.journal_ui.listWidget.addItem(display_text)
        else:
            QtWidgets.QMessageBox.critical(
                self.window, "Error",
                f"Failed to load journal entries: {result['error']}"
            )
