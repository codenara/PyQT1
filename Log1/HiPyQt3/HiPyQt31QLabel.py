# HiPyQt version 3.1
# use QLabel
# use QPushButton

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # QLabel
        self.label = QLabel("QLabel", self)
        self.label.move(20, 60)
        self.label.resize(150, 30)

        # QPushButton
        self.button = QPushButton("Label", self)
        self.button.move(20, 20)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        if self.label.text() == "":
            self.label.setText("QLabel")
        else:
            self.label.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
