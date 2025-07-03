from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # QListWidget instead of QTableView
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 80, 781, 461))
        self.listWidget.setObjectName("listWidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 511, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.doctype_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.doctype_label.setFont(font)
        self.doctype_label.setObjectName("doctype_label")
        self.horizontalLayout.addWidget(self.doctype_label)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(540, 20, 251, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.add_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout_2.addWidget(self.add_button)

        self.actions_dropdown = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.actions_dropdown.setObjectName("actions_dropdown")
        self.actions_dropdown.addItem("")
        self.actions_dropdown.addItem("")
        self.actions_dropdown.addItem("")
        self.actions_dropdown.addItem("")
        self.horizontalLayout_2.addWidget(self.actions_dropdown)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.doctype_label.setText(_translate("MainWindow", "Doctype Name"))
        self.add_button.setText(_translate("MainWindow", "Add New"))
        self.actions_dropdown.setItemText(0, _translate("MainWindow", "Edit"))
        self.actions_dropdown.setItemText(1, _translate("MainWindow", "Cancel"))
        self.actions_dropdown.setItemText(2, _translate("MainWindow", "Duplicate"))
        self.actions_dropdown.setItemText(3, _translate("MainWindow", "Delete"))
