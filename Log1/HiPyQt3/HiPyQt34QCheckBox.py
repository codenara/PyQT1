# HiPyQt version 3.4
# use QGroupBox
# use QCheckBox
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
        self.groupBox.resize(380, 120)

        # CheckBox1
        self.checkBox1 = QCheckBox("CheckBox1", self)
        self.checkBox1.move(20, 20)
        self.checkBox1.resize(150, 30)
        self.checkBox1.stateChanged.connect(self.checkBox_stateChanged)

        # CheckBox2
        self.checkBox2 = QCheckBox("CheckBox2", self)
        self.checkBox2.move(20, 50)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBox_stateChanged)

        # CheckBox3
        self.checkBox3 = QCheckBox("CheckBox3", self)
        self.checkBox3.move(20, 80)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBox_stateChanged)

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBox_stateChanged(self):
        msg = ""
        if self.checkBox1.isChecked() == True:
            msg += "CheckBox1 "
        if self.checkBox2.isChecked() == True:
            msg += "CheckBox2 "
        if self.checkBox3.isChecked() == True:
            msg += "CheckBox3"
        self.statusBar.showMessage(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
