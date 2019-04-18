# HiPyQt version 1.1

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle("Hi QWidget")
widget.setGeometry(50, 50, 400, 300)
widget.show()

window = QMainWindow()
window.setWindowTitle("Hi QMainWindow")
window.setGeometry(100, 100, 400, 300)
window.show()

dialog = QDialog()
dialog.setWindowTitle("Hi QDialog")
dialog.setGeometry(150, 150, 400, 300)
dialog.show()

label = QLabel("Life is short\nYou need Python")
label.setWindowTitle("Hi QLabel")
label.show()

button = QPushButton("Click Me")
button.setWindowTitle("Hi QPushButton")
button.show()

app.exec()
