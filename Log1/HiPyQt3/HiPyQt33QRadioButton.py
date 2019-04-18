# HiPyQt version 3.3
# use QGroupBox
# use QRadioButton
# use QStatusBar

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # GroupBox
        self.groupBox = QGroupBox("GroupBox", self)
        self.groupBox.move(10, 10)
        self.groupBox.resize(380, 80)

        # RadioButton1
        self.radioButton1 = QRadioButton("RadioButton1", self)
        self.radioButton1.move(20, 20)
        self.radioButton1.clicked.connect(self.radioButton_clicked)
        self.radioButton1.setChecked(True)

        # RadioButton2
        self.radioButton2 = QRadioButton("RadioButton2", self)
        self.radioButton2.move(20, 40)
        self.radioButton2.clicked.connect(self.radioButton_clicked)

        # RadioButton3
        self.radioButton3 = QRadioButton("RadioButton3", self)
        self.radioButton3.move(20, 60)
        self.radioButton3.clicked.connect(self.radioButton_clicked)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def radioButton_clicked(self):
        if self.radioButton1.isChecked():
            self.statusBar.showMessage("RadioButton1")
        elif self.radioButton2.isChecked():
            self.statusBar.showMessage("RadioButton2")
        else:
            self.statusBar.showMessage("RadioButton3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
