import sys
from kiwoom.kiwoom import *
from kiwoom.login.Login import *
from PyQt5.QtWidgets import *

class Main():
    def __init__(self):
        print("Main() start")
        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom() #키움 클래스 객체화
        self.app.exec_() #이벤트 루프 실행

if __name__ == "__main__":
        Main()



