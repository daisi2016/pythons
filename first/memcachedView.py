# coding=UTF-8
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *
import memcache
qt_app = QApplication(sys.argv)

class Memcached(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Memcached View')
        self.setMinimumWidth(400)
        self.setMinimumHeight(350)
        self.setMaximumWidth(400)
        self.setMaximumHeight(350)
        icon = QIcon()
        icon.addPixmap(QPixmap('D:\\workspace\\python\\first\\2.ico'), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ip = QLineEdit(self)
        self.ip.setPlaceholderText('ip地址'.decode('UTF-8'))
        self.ip.setText('10.10.12.87')
        self.form_layout.addRow('地址1：'.decode('UTF-8'), self.ip)

        self.port = QLineEdit(self)
        self.port.setPlaceholderText('端口1'.decode('UTF-8'))
        self.port.setText('11411')
        self.form_layout.addRow('端口1：'.decode('UTF-8'), self.port)

        self.ip2 = QLineEdit(self)
        self.ip2.setPlaceholderText('ip地址'.decode('UTF-8'))
        self.ip2.setText('10.10.12.87')
        self.form_layout.addRow('地址2：'.decode('UTF-8'), self.ip2)

        self.port2 = QLineEdit(self)
        self.port2.setPlaceholderText('端口2'.decode('UTF-8'))
        self.port2.setText('11511')
        self.form_layout.addRow('端口2：'.decode('UTF-8'), self.port2)

        self.types = [
                            'SCOS业务参数'.decode('UTF-8'),
                            '普通缓存'.decode('UTF-8')
                            ]
        self.type = QComboBox(self)
        self.type.addItems(self.types)
        self.form_layout.addRow('参数类型：'.decode('UTF-8'), self.type)

        self.key = QLineEdit(self)
        self.key.setPlaceholderText('memcached key')
        self.form_layout.addRow('KEY:', self.key)

        self.memValue = QTextEdit(self)
        self.form_layout.addRow('VALUE:', self.memValue)

        self.layout.addLayout(self.form_layout)

        self.layout.addStretch(1)

        self.button_box = QHBoxLayout()

        self.button_box.addStretch(1)

        self.searchButton = QPushButton('查询'.decode('UTF-8'), self)
        self.searchButton.clicked.connect(self.search)
        self.button_box.addWidget(self.searchButton)

        self.layout.addLayout(self.button_box)

        self.setLayout(self.layout)

    def run(self):
        self.show()
        qt_app.exec_()

    @Slot()
    def search(self):
        # self.client = Client((self.ip.text(), self.port.text()))
        # self.result =  self.client.get(self.key.text())
        #client = Client(('10.10.12.87',11511))
        #result = client.get('queryFlag')

        #client1 = HashClient([('10.10.12.87', 11411), ('10.10.12.87', 11511)])
        #result = client1.get('scos-zdCustCheckTime')
        #print (result)
        self.memValue.setText('')
        client=memcache.Client([self.ip.text()+':'+self.port.text(),self.ip2.text()+':'+ self.port2.text()], debug=0)
        index = self.type.currentIndex()

        #print (client.get_stats('statsItems'))
        #print (client.get_stats('keys'))

        if(index==0):
          #  print(client.get_slab_stats())
            result = client.get('scos-'+self.key.text())
        else:
            result = client.get(self.key.text())
        print(result)
        self.memValue.setText(result)
        client.disconnect_all()



    # Create an instance of the application window and run it
app = Memcached()
app.run()