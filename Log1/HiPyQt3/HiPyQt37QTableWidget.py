# HiPyQt version 3.7
# use QTableWidget
# use QCheckBox

import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hi PyQt")
        self.setGeometry(50, 50, 400, 300)

        # QTableWidget
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resize(290, 290)
        self.tableWidget.setRowCount(2)
        self.tableWidget.setColumnCount(2)

        self.tableWidget.setItem(0, 0, QTableWidgetItem("(0,0)"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("(0,1)"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("(1,0)"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("(1,1)"))

        # CheckBox
        self.checkBox = QCheckBox("Editable", self)
        self.checkBox.move(300, 20)
        self.checkBox.resize(90, 30)
        self.checkBox.stateChanged.connect(self.checkBox_stateChanged)

    def checkBox_stateChanged(self):
        if self.checkBox.isChecked() == True:
            self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)  # Enable editing
        else:
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable editing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
