from UI.Sources.ui.Login import Ui_Form
import requests,re
from PyQt5.Qt import *
class Window(QWidget,Ui_Form):
    def setupUi(self, Form):
        super().__init__()
        self.setupUi(self)

    def Login(self):
        # 模拟登录函数，用户名，密码正确，返回错误标志位，登录新界面的 Html text ，Cookie
        cookieFlag,cookies = self.getCookie()

        if cookieFlag == False:
            # 提示用户名或者密码错误
            pass
        else:
            print(cookies)
            # 得到cookie字典进入下个界面

    def getCookie(self):
        # 获取cookie函数，如果用户名，密码错误，errorFlag返回False，并且cookie为空
        errorFlag = False
        data = {
            'Login1$_txtAccount': self.userName.get(),
            'Login1$_txtPWD': '',
            '__VIEWSTATE': '/wEPDwUKLTQ1NTkwODAyMg9kFgICAw9kFgQCAQ9kFg4CBQ8PFgIeBFRleHQFM+W9k+WJjTxmb250IGNvbG9yPSIjY2MwMDAwIj4xPC9mb250PuS9jeeUqOaIt+WcqOe6v2RkAgcPDxYCHwAFBzxiPjwvYj5kZAIJDw8WAh4HVmlzaWJsZWhkZAIKDw8WBB8ABQXCoHzCoB8BaGRkAgsPDxYEHwAFBuWkluWHuh4LTmF2aWdhdGVVcmwFFC4uL0NvbW1vbi9MZWF2ZS5hc3B4ZGQCDQ8PFgIfAAUG5biQ5Y+3ZGQCDw8PFgIfAAUG6YCA5Ye6ZGQCAw9kFgICBA8PFgIfAAUb55So5oi35ZCN5oiW5a+G56CB5pyJ6K+v77yBZGRktThqfHvDjJayCu2Ywmisa6gVkQk=',
            '__EVENTVALIDATION': '/wEWBQLupKneDAKTup+7CgKdu4mlDQLzuILQCgLbqb+1DIuL2a5Sf0hGICaCq32juFgb4ssf',
            'Login1$_btnWebLogin': '登录(zh-chs)'
        }
        # allow_redirects 重定向使能，一般登录时，用户端会将用户名，密码等信息上传至服务器，服务器返回cookie，或者令牌token 给用户端
        # 返回方式为重定向，用抓包工具可知此时状态码为302 ， request库默认 allow_redirects=Ture 允许自动重定向，resp得到的是重定向之后的200的HTML内容
        resp = requests.post(extranetlUrl['login'], data,allow_redirects=False,timeout=30)
        resp.raise_for_status()
        if resp.status_code == 302:
            # 查看网页，寻找规律发现302，为用户名，密码正确，且服务器设置用户端cookie
            resp.encoding = resp.apparent_encoding
            # str = requests.utils.dict_from_cookiejar(resp.cookies)              # 获取cookie字符串
            # # 组合成字符串字典
            # cookies = {}
            # for line in str.split(';'):
            #     key, value = line.split('=', 1)
            #     cookies[key] = value
            #
            errorFlag = True
            return errorFlag,requests.utils.dict_from_cookiejar(resp.cookies)
        elif resp.status_code ==200:
            # 分析网页可得，状态码为200时，用户名或者密码错误
            errorFlag = False
            return errorFlag,''

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    window = Window()
    window.setupUi(Form,Ui_Form)
    extranetlUrl = {
        'login': 'http://rdm.toptech-developer.com:81/BPM/Home/Login.aspx?ReturnUrl=/bpm/TaskList/Default.aspx',
        'taskList': 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx',
        'newTask': '',

    }
    sys.exit(app.exec_())