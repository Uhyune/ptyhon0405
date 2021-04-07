#화면단(DemoForm2.ui) + 로직단(DemoForm2.py)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#미리 만든 화면을 로딩(두번째 화면)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#다이얼로그를 상속받아서 폼 클래스를 정의
class DemoForm(QMainWindow,form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #시그널을 처리하는 슬롯메서드
    def firstClick(self):
        self.label.setText("첫번째 클릭")
    def secondClick(self):
        self.label.setText("두번째 클릭")
    def thirdClick(self):
        self.label.setText("세번째 클릭")

#직접 이 모듈을 실행했는지 진입점 (entry point) 체크
if __name__ == "__main__" :
    #실행 프로세스를 실행 (python.exe)
    app = QApplication(sys.argv)
    #위에 있는 클래스의 인스턴스를 생성
    demoWindow = DemoForm()
    #창을 보여달라
    demoWindow.show()
    #지속적으로 실행(이벤트 루프)
    app.exec_()