# HiPyQt version 2.0

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # Button
        self.button = QPushButton("Click Me", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QMessageBox.about(self, "Hi PyQt", "Life is short\nYou need Python")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
