from UI.Sources.ui.taskList_UI import Ui_TaskListWindow
from PyQt5.Qt import *
from PyQt5 import QtWidgets
from PyQt5.QtWebEngineWidgets import *

class TaskList(QWidget,Ui_TaskListWindow):

    listChoose_comb_change_signal = pyqtSignal(str,str)
    refreshWebtext_signal = pyqtSignal()
    #
    # 设置网页在窗口中显示的位置和大小
    # self.qwebengine.setGeometry(20, 20, 600, 600)
    # # 在QWebEngineView中加载网址
    # self.qwebengine.load(QUrl(r"https://www.csdn.net/"))

    def __init__(self,webtext,displayList,cookies):
        super().__init__()
        self.webtext = webtext
        self.displayList = displayList
        self.cookies = cookies
        self.setupUi(self)
        self.taskList_btn.setChecked(True)              # 设置待处理任务按钮选中
        self.btn_checkFalse('taskList_btn')             # 设置填写新表单等按钮取消
        self.taskInformation_btn.setChecked(True)       # 设置订单信息按钮选中
        self.waring_btn.setChecked(False)               # 设置注意事项按钮取消
        self.add_btn.setHidden(True)                    # 设置注意事项增加按钮隐藏
        self.delete_btn.setHidden(True)                 # 设置注意事项增加按钮隐藏

        # 设置水平布局盒子，并命名为horizontalLayout3
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.Web_wid)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        # 创建QWebEngineView 控件
        self.qwebengine = QWebEngineView()
        #self.qwebengine.setParent(self.Web_wid)
        # 往Bottom 窗口添加 QWebEngineView 控件，并实现水平布局
        self.horizontalLayout3.addWidget(self.qwebengine)
        QWebEngineProfile.defaultProfile().setHttpUserAgent('Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6')
        # 清除COOKIE
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        # 设置隐藏
        self.Web_wid.setHidden(True)

        self.setMouseTracking(True)

    def mouseMoveEvent(self,event):
        if self.Top_wid.hide() :
            self.Top_wid.setHidden(False)
        else:
            self.Top_wid.setHidden(True)

    def listChoose_comb_change(self):
        if self.taskList_btn.isChecked():
            if self.taskInformation_btn.isChecked() and not self.waring_btn.isChecked():  # 查看电子流信息
                text = self.listChoose_comb.currentText()
                self.listChoose_comb_change_signal.emit(self.webtext,text)

    def newForm_btn_click(self,checked):

        self.setMouseTracking(True)
        if checked:
            # 其他按钮隐藏
            self.btn_checkFalse('newForm_btn')
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)

            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx"))
            self.qwebengine.load(QUrl(r"http://rdm.toptech-developer.com:81/bpm/PostRequest/Default.aspx"))

    def draft_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('draft_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)
            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/TaskList/Draft.aspx"))
            self.qwebengine.load(QUrl((r"http://rdm.toptech-developer.com:81/bpm/TaskList/Draft.aspx")))

    def taskList_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            # 界面互动
            self.btn_checkFalse('taskList_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(False)
            self.Table_veiw_wid.setHidden(False)
            self.Web_wid.setHidden(True)

    def historicalSen_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('historicalSen_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)
            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/History/My.aspx"))
            self.qwebengine.load(QUrl((r"http://rdm.toptech-developer.com:81/bpm/History/My.aspx")))

    def historicalPro_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('historicalPro_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)
            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/History/Processed.aspx"))
            self.qwebengine.load(QUrl((r"http://rdm.toptech-developer.com:81/bpm/History/Processed.aspx")))

    def Form_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('Form_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)
            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/Reports/Default.aspx"))
            self.qwebengine.load(QUrl((r"http://rdm.toptech-developer.com:81/bpm/Reports/Default.aspx")))

    def lookFor_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('lookFor_btn')
            #self.showMinimized()
            self.Left_wid.setHidden(True)
            self.Table_veiw_wid.setHidden(True)
            self.Web_wid.setHidden(False)
            for key in self.cookies:
                cookie = QNetworkCookie(QByteArray(key.encode()), QByteArray(self.cookies[key].encode()))
                QWebEngineProfile.defaultProfile().cookieStore().setCookie(cookie, QUrl(r"http://rdm.toptech-developer.com:81/bpm/History/All.aspx"))
            self.qwebengine.load(QUrl((r"http://rdm.toptech-developer.com:81/bpm/History/All.aspx")))

    def taskInformation_btn_click(self,checked):
        if checked :
            self.listChoose_comb.setEnabled(True)               # 设置生产指示单下拉框打开
            self.waring_btn.setChecked(False)
        else:
            self.listChoose_comb.setEnabled(False)              # 设置生产指示单下拉框禁止

    def waring_btn_click(self,checked):
        if checked:
            self.listChoose_comb.setEnabled(False)              # 设置生产指示单下拉框禁止
            self.taskInformation_btn.setChecked(False)

    def btn_checkFalse(self,set_btn_checkFalse):
        #

        chooseList = ['newForm_btn','draft_btn','taskList_btn','historicalSen_btn','historicalPro_btn','Form_btn','lookFor_btn']

        # 列表根据值删除，其他方法还有根据index 删除列表元素del，pop等
        chooseList.remove(set_btn_checkFalse)
        widget = self.Top_wid

        # 遍历widget内所有控件
        for btn in widget.children():
            if btn.objectName() in chooseList:
                #print(btn.objectName())
                btn.setChecked(False)

    def displayTablelist(self,displayList):

        if len(displayList) != 0:

            self.displayPro_labe.setText('待处理任务:[%s/%s]' % (len(displayList),len(displayList)))

            # 设置数据层次结构，4行4列
            self.tableView.model = QStandardItemModel(len(displayList), len(displayList[0])-2)
            # 设置水平方向四个头标签文本内容
            self.tableView.model.setHorizontalHeaderLabels(['流水号', '流程名称', '所有人', '发起时间','当前步骤','摘要信息'])

            # Todo 优化2 添加数据
            # self.model.appendRow([
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            # ])

            for row in range(len(displayList)):
                for column in range(len(displayList[0])-2):

                    if column == (len(displayList[0])-1) :
                        item = QStandardItem(displayList[row][column])
                    else:
                        item = QStandardItem(displayList[row][column])
                    # 设置每个位置的文本值
                    self.tableView.model.setItem(row, column, item)

            self.tableView.setModel(self.tableView.model)

            #todo 优化1 表格填满窗口
            #水平方向标签拓展剩下的窗口部分，填满表格
            self.tableView.horizontalHeader().setStretchLastSection(True)
            #水平方向，表格大小拓展到适当的尺寸
            self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            # 设定列宽
            # self.tableView.setColumnWidth(0, 110)
            # self.tableView.setColumnWidth(1, 70)
            # self.tableView.setColumnWidth(2, 120)
            # self.tableView.setColumnWidth(3, 140)
            # self.tableView.setColumnWidth(4, 70)

            for i in range(5):
                self.tableView.horizontalHeader().setSectionResizeMode(i,QHeaderView.ResizeToContents)


            # #TODO 优化3 删除当前选中的数据
            # indexs=self.tableView.selectionModel().selection().indexes()
            # print(indexs)
            # if len(indexs)>0:
            #     index=indexs[0]
            #     self.model.removeRows(index.row(),1)

    def refreshWebtext(self):
        self.refreshWebtext_signal.emit()
