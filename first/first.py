# Allow access to command-line arguments
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *

# Every Qt application must have one and only one QApplication object;
# it receives the command line arguments passed to the script, as they
# can be used to customize the application's appearance and behavior
qt_app = QApplication(sys.argv)
parent_widget = QWidget()
parent_widget.setMinimumSize(QSize(800, 600))
parent_widget.setWindowTitle('memcached')
# Create a label widget with our text
label = QLabel('Hello, world!', parent_widget)
label.setMinimumSize(QSize(200,300))
# Show it as a standalone widget
parent_widget.show()

# Run the application's event loop
qt_app.exec_()




