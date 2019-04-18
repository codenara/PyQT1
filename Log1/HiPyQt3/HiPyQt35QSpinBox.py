# HiPyQt version 3.5
# use QSpinBox
# use QStatusBar

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # QSpinBox
        self.spinBox = QSpinBox(self)
        self.spinBox.move(10, 10)
        self.spinBox.resize(80, 22)
        self.spinBox.valueChanged.connect(self.spinBox_valueChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def spinBox_valueChanged(self):
        val = str(self.spinBox.value())
        self.statusBar.showMessage(val)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
