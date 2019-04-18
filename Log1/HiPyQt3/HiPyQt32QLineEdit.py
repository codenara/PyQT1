# HiPyQt version 3.2
# use QLineEdit
# use QStatusBar

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # LineEdit
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(20, 20)
        self.lineEdit.textChanged.connect(self.lineEdit_textChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEdit_textChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
