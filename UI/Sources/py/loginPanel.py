from UI.Sources.ui.login_UI import Ui_Form
from PyQt5.Qt import *
class LoginPanel(QWidget,Ui_Form):
    check_login_Btn_signal = pyqtSignal(str,str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def check_login_Btn(self):
        account = self.userName.currentText()
        pwd = self.passWord.text()
        self.check_login_Btn_signal.emit(account,pwd)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = LoginPanel()
    window.show()
    sys.exit(app.exec_())