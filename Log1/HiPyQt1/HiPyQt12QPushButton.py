# HiPyQt version 1.2

import sys
from PyQt5.QtWidgets import *


def button_clicked():
    print('Clicked')


app = QApplication(sys.argv)
button = QPushButton("Click Me")
button.clicked.connect(button_clicked)
button.show()
app.exec()
