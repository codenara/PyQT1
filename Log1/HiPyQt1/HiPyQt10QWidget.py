# HiPyQt version 1.0

import sys
from PyQt5.QtWidgets import *

print(sys.version)
print(sys.argv)

app = QApplication(sys.argv)

widget = QWidget()
widget.setWindowTitle("Hi QWidget")
widget.setGeometry(50, 50, 400, 300)
widget.show()

app.exec()
