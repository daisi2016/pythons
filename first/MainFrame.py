import sys
from PySide.QtGui import *
from dialog_ui import Ui_Dialog

qt_app = QApplication(sys.argv)

dialog = Ui_Dialog(qt_app)
dialog.show()
sys.exit(qt_app.exec_())

