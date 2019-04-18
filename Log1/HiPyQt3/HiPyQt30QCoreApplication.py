# HiPyQt version 3.0
# use QPushButton

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # Button
        self.button = QPushButton("Close", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        QCoreApplication.instance().quit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
