import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp,QToolTip, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import *

class MyApp(QMainWindow):

   def __init__(self):
        super().__init__()
        self.initUI()

   def initUI(self):
        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        btn.move(50, 150)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(150, 150)
        btn.resize(btn.sizeHint())

        self.statusBar().showMessage('Ready')

        now = QDate.currentDate()
        print(now.toString())

        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('img/web.png'))
        self.setGeometry(300, 300, 300, 200)
        self.move(300, 300)
        self.center()
        self.resize(400, 200)
        self.show()

   def center(self):
       qr = self.frameGeometry()
       cp = QDesktopWidget().availableGeometry().center()
       qr.moveCenter(cp)
       self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())