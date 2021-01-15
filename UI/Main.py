from UI.Sources.py.loginPanel import LoginPanel
from UI.Sources.py.tasklistPanel import TaskList
from UI.Sources.py.excelPandas import dataAnalysis
from UI.Sources.py.addwarinformationPanel import Addwarinf
from PyQt5.Qt import *
from Parsing_RDM import WebText
import numpy as np

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
        'nextweb':'http://rdm.toptech-developer.com:81/bpm/XMLService/DataProvider.aspx',
        'backlist':'http://rdm.toptech-developer.com:81/bpm/Common/RecedeBackSelStep.aspx?pid=',
        'newTask': '',
    }
    intranetUrl = {
        'login': 'http://172.168.5.151:81/bpm/Home/Login.aspx',
        'taskList': 'http://172.168.5.151:81/bpm/PostRequest/Default.aspx',
        'nextweb':'http://172.168.5.151:81/bpm/XMLService/DataProvider.aspx',
        'backlist': 'http://172.168.5.151:81/bpm/Common/RecedeBackSelStep.aspx?pid=',
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

    def displaychange(webtext,listChoose_comb_Text):
        list,pid,tid = rdmWeb.getsolist(webtext,listChoose_comb_Text)
        # 生产指示单需要保存订单详细信息
        if listChoose_comb_Text == "生产指示单":
            soList = rdmWeb.getSoinformation(extranetlUrl['nextweb'],pid)
            back_list = rdmWeb.getbacklist(extranetlUrl['backlist'],pid)
            # 保存记录订单信息
            if len(soList)>0:
                data.solist_to_excel(soList,back_list)
            # 显示信息
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
        Data = data.getSourcedata('WaringInformation','')
        tasklistpanel.displayTablelist(Data.values,Data.columns.values)

    def addWarinformation(projectName,projectNum,projectSpec):
        addwarinf.projectName_Ledit.setText(projectName)
        addwarinf.projectNum_Ledit.setText(projectNum)
        addwarinf.projectSpec_Ledit.setText(projectSpec)
        addwarinf.show()
        addwarinf.search_btn.click()

    def delNumList(delList):
        sourcedata = data.getSourcedata('WaringInformation','')
        result = data.deldata(sourcedata,delList)

    def addData(addData):
        # 处理pandas数据
        data.add_data(addData)
        # 显示
        diswaringInformation()

    def closeAddwindow():
        diswaringInformation()

    def dispaly_tab_InsertData(appendRow,so_no):
        # 根据SO判断年月
        so_year = '20' + so_no[2:4]
        soInformation = data.getSourcedata(so_year,'sheet1')
        # 选取部分数据getSourcedata
        insertData = soInformation[['SO号','成品料号','成品名称','成品规格']]
        # 筛选数据，得到对应SO的订单信息
        insertData = insertData[insertData['SO号'] == so_no]
        # 删除多余信息（SO号）,并转化成list
        insertData = insertData.iloc[:,1:].values[0]

        # 二、提取警告信息
        waringInformation = data.getSourcedata('WaringInformation','')
        waringInformation = waringInformation[waringInformation['ProjectNum'] == insertData[0]]
        print(waringInformation)
        waringStr = str(waringInformation['waringInformation'].values)[2:-2]

        tasklistpanel.insert_display(appendRow,insertData,waringStr)

    #信号连接
    loginpanel.check_login_Btn_signal.connect(login)
    tasklistpanel.listChoose_comb_change_signal.connect(displaychange)
    tasklistpanel.refreshWebtext_signal.connect(newWebtext)
    tasklistpanel.search_btn_click_signal.connect(searchProjectNum)
    tasklistpanel.waring_btn_click_signal.connect(diswaringInformation)
    tasklistpanel.add_btn_click_signal.connect(addWarinformation)
    tasklistpanel.del_btn_click_signal.connect(delNumList)
    tasklistpanel.display_tab_right_click_signal.connect(dispaly_tab_InsertData)
    addwarinf.addwindow_search_btn_click_signal.connect(searchProjectNum)
    addwarinf.addwindow_combit_btn_click_signal.connect(addData)
    addwarinf.addwindow_close_signal.connect(closeAddwindow)


    loginpanel.show()
    sys.exit(app.exec_())



