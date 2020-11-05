import os
import sys
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *
from config.errorCode import *
from PyQt5.QtTest import *
from config.kiwoomType import *
from config.log_class import *

class Login:
    def __init__(self):
        self.loginEventLoop = QEventLoop()  # 로그인 요청용 이벤트루프
        self.initOcxInstance()  # OCX 방식을 파이썬에 사용할 수 있게 변환해 주는 함수
        self.eventSlots()  # 키움과 연결하기 위한 시그널 / 슬롯 모음
        self.connect()

    def initOcxInstance(self):
        self.setControl("KHOPENAPI.KHOpenAPICtrl.1") #OCX 방식을 파이썬에 사용할 수 있게 반환해 주는 함수 실행

    def eventSlots(self):
        self.OnEventConnect.connect(self.loginSlot)  # 로그인 관련 이벤트

    def connect(self, evtLoop):
        print("kiwoom.Login() class start.")
        self.dynamicCall("CommConnect()")
        self.loginEventLoop.exec_()  # 이벤트루프 실행

    def loginSlot(self, err_code):
        self.logging.logger.debug(errors(err_code)[1])
        self.loginEventLoop.exit() #이벤트루프 종료