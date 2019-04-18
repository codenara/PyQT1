# HiPyQt version 3.8
# use QTableWidget
# use QCheckBox
# use QPushButton

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

        self.tableWidget.setItem(0, 0, QTableWidgetItem("John"))
        self.tableWidget.setItem(0, 1, QTableWidgetItem("21"))
        self.tableWidget.setItem(1, 0, QTableWidgetItem("Paul"))
        self.tableWidget.setItem(1, 1, QTableWidgetItem("22"))

        horizontalHeaderLabels = ["Name", "Age"]
        self.tableWidget.setHorizontalHeaderLabels(horizontalHeaderLabels)
        verticalHeaderLabels = ["One", "Two"]
        self.tableWidget.setVerticalHeaderLabels(verticalHeaderLabels)

        # QCheckBox
        self.checkBox = QCheckBox("Editable", self)
        self.checkBox.move(300, 10)
        self.checkBox.resize(90, 30)
        self.checkBox.stateChanged.connect(self.checkBox_stateChanged)

        # QPushButton
        self.button = QPushButton("Resize", self)
        self.button.move(300, 50)
        self.button.resize(80, 30)
        self.button.clicked.connect(self.button_clicked)

    def checkBox_stateChanged(self):
        if self.checkBox.isChecked() == True:
            self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)  # Enable editing
        else:
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  # Disable editing

    def button_clicked(self):
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
