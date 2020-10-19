from UI.Sources.py.loginPanel import LoginPanel
from UI.Sources.py.tasklistPanel import TaskList
from PyQt5.Qt import *
from Parsing_RDM import WebText

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    loginpanel = LoginPanel()
    tasklistpanel = TaskList('','','')     # webtext,displayList
    rdmWeb = WebText('','')             # webtext,cookies
    extranetlUrl = {
        'login': 'http://rdm.toptech-developer.com:81/BPM/Home/Login.aspx?ReturnUrl=/bpm/TaskList/Default.aspx',
        'taskList': 'http://rdm.toptech-developer.com:81/bpm/TaskList/Default.aspx',
        'newTask': '',
    }

    intranetUrl = {
        'login': 'http://172.168.5.151:81/bpm/Home/Login.aspx',
        'taskList': 'http://172.168.5.151:81/bpm/PostRequest/Default.aspx',
        'newTask': '',
    }

    headers = {'Referer': 'http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6', }

    # 槽函数
    def login(account,pwd):
        errorFlag, Cookies = rdmWeb.getCookie(extranetlUrl["login"],account,pwd)
        rdmWeb.cookies = Cookies

        # 传递cookie给TaskList界面
        tasklistpanel.cookies = Cookies
        print(Cookies)
        if errorFlag == True :
            loginpanel.hide()
            webtext = rdmWeb.gethtmltext("get",extranetlUrl['taskList'], **headers)
            rdmWeb.webtext = webtext
            tasklistpanel.webtext = webtext
            tasklistpanel.listChoose_comb_change()
            tasklistpanel.show()
        else:
            print("用户名或密码错误！")


    def displaychange(webtext,liststr):
        list = rdmWeb.getsolist(webtext,liststr)
        tasklistpanel.displayTablelist(list)

    def newWebtext():
        newWebtext = rdmWeb.gethtmltext("get", extranetlUrl['taskList'], **headers)
        rdmWeb.webtext = newWebtext
        tasklistpanel.webtext = newWebtext
        tasklistpanel.listChoose_comb_change()


    #信号连接
    loginpanel.check_login_Btn_signal.connect(login)
    tasklistpanel.listChoose_comb_change_signal.connect(displaychange)
    tasklistpanel.refreshWebtext_signal.connect(newWebtext)


    loginpanel.show()
    sys.exit(app.exec_())



