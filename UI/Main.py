from UI.Sources.py.loginPanel import LoginPanel
from UI.Sources.py.tasklistPanel import TaskList
from UI.Sources.py.excelPandas import dataAnalysis
from UI.Sources.py.addwarinformationPanel import Addwarinf
from PyQt5.Qt import *
from Parsing_RDM import WebText

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    loginpanel = LoginPanel()
    tasklistpanel = TaskList('',[],{})     # webtext,displayLis
    addwarinf = Addwarinf()
    # 设置鼠标跟踪
    tasklistpanel.setMouseTracking(True)
    rdmWeb = WebText('',{})             # webtext,cookies
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
    data = dataAnalysis("", "", "")

    # 槽函数
    def login(account,pwd):
        errorFlag, Cookies = rdmWeb.getCookie(extranetlUrl["login"],account,pwd)
        rdmWeb.cookies = Cookies

        # 传递cookie给TaskList界面
        tasklistpanel.cookies = Cookies
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
        if list.shape[0] !=0:
            header = ['流水号', '流程名称', '所有人', '发起时间','当前步骤','摘要信息']
            tasklistpanel.displayTablelist(list[:,:-2],header)
        else:
            tasklistpanel.displayTablelist([], [])

    def newWebtext():
        newWebtext = rdmWeb.gethtmltext("get", extranetlUrl['taskList'], **headers)
        rdmWeb.webtext = newWebtext
        tasklistpanel.webtext = newWebtext
        tasklistpanel.listChoose_comb_change()

    def searchProjectNum(projectName,projectNum,projectSpec,fileName):
        dataFilter,datafiltCol =data.Screen(projectName,projectNum,projectSpec,fileName)
        if fileName =="WaringInformation":
            if dataFilter.shape[0] != 0:
                tasklistpanel.add_btn.setEnabled(False)
                tasklistpanel.del_btn.setEnabled(True)
                tasklistpanel.allChoose_Rad.setEnabled(True)
                tasklistpanel.inverse_Rad.setEnabled(True)
                tasklistpanel.displayTablelist(dataFilter,datafiltCol)
            else:
                tasklistpanel.allChoose_Rad.setEnabled(False)
                tasklistpanel.inverse_Rad.setEnabled(False)
                tasklistpanel.add_btn.setEnabled(True)
                tasklistpanel.del_btn.setEnabled(False)
                tasklistpanel.displayTablelist([], [])
        elif fileName == "Lib":
            if dataFilter.shape[0] != 0:
                addwarinf.waringIforma_Ledit.setEnabled(True)
                addwarinf.commit_btn.setEnabled(True)
                addwarinf.allChoose_Rad.setEnabled(True)
                addwarinf.inverse_Rad.setEnabled(True)
                addwarinf.displayTablelist(dataFilter,datafiltCol)
            else:
                addwarinf.waringIforma_Ledit.setEnabled(False)
                addwarinf.commit_btn.setEnabled(False)
                addwarinf.allChoose_Rad.setEnabled(False)
                addwarinf.inverse_Rad.setEnabled(False)
                addwarinf.displayTablelist([],[])

    def diswaringInformation():
        Data = data.getSourcedata('WaringInformation')
        tasklistpanel.displayTablelist(Data.values,Data.columns.values)

    def addWarinformation(projectName,projectNum,projectSpec):
        addwarinf.projectName_Ledit.setText(projectName)
        addwarinf.projectNum_Ledit.setText(projectNum)
        addwarinf.projectSpec_Ledit.setText(projectSpec)
        addwarinf.show()
        addwarinf.search_btn.click()

    def delNumList(delList):
        sourcedata = data.getSourcedata('WaringInformation')
        result = data.deldata(sourcedata,delList)

    def addData(addData):
        # 处理pandas数据
        data.add_data(addData)
        # 显示
        diswaringInformation()

    def closeAddwindow():
        diswaringInformation()

    #信号连接
    loginpanel.check_login_Btn_signal.connect(login)
    tasklistpanel.listChoose_comb_change_signal.connect(displaychange)
    tasklistpanel.refreshWebtext_signal.connect(newWebtext)
    tasklistpanel.search_btn_click_signal.connect(searchProjectNum)
    tasklistpanel.waring_btn_click_signal.connect(diswaringInformation)
    tasklistpanel.add_btn_click_signal.connect(addWarinformation)
    tasklistpanel.del_btn_click_signal.connect(delNumList)
    addwarinf.addwindow_search_btn_click_signal.connect(searchProjectNum)
    addwarinf.addwindow_combit_btn_click_signal.connect(addData)
    addwarinf.addwindow_close_signal.connect(closeAddwindow)


    loginpanel.show()
    sys.exit(app.exec_())



