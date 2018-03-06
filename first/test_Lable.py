# Allow access to command-line arguments
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

qt_app = QApplication(sys.argv)

class Testlable(QLabel):
    def __init__(self):
            QLabel.__init__(self,'hello world')
            self.setMinimumSize(QSize(800,800))
            self.setAlignment(Qt.AlignCenter)
            self.setWindowTitle('test')

    def run(self):
             self.show()
             qt_app.exec_()

Testlable().run()
