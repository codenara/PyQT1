# HiPyQt version 2.1

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi QDialog")
        self.setGeometry(150, 150, 400, 300)
        self.setWindowModality(Qt.ApplicationModal)

        self.button = QPushButton("Click Me", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QMessageBox.about(self, "Hi PyQt", "Life is short\nYou need Python")


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # Button
        self.button = QPushButton("Show Dialog", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        myDialog = MyDialog()
        myDialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
