from UI.Sources.ui.taskList_UI import Ui_TaskListWindow
from PyQt5.Qt import *
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWebEngineWidgets import *

class TaskList(QWidget,Ui_TaskListWindow):

    listChoose_comb_change_signal = pyqtSignal(str, str)
    refreshWebtext_signal = pyqtSignal()
    search_btn_click_signal = pyqtSignal(str, str, str,str)
    waring_btn_click_signal = pyqtSignal()
    add_btn_click_signal = pyqtSignal(str, str, str)
    del_btn_click_signal = pyqtSignal(list)

    def __init__(self,webtext,displayList,cookies):
        # 基本参数初始化
        super().__init__()
        self.webtext = webtext
        self.displayList = displayList
        self.cookies = cookies
        self.setupUi(self)
        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)  # 去掉标题栏
        # 窗口控件状态初始化
        self.taskList_btn.setChecked(True)              # 设置待处理任务按钮选中
        self.btn_checkFalse('taskList_btn')             # 设置填写新表单等按钮取消
        self.taskInformation_btn.setChecked(True)       # 设置订单信息按钮选中
        self.waring_btn.setChecked(False)               # 设置注意事项按钮取消
        self.pcbInformation_btn.setChecked(False)       # 设置未下PCB订单按钮取消
        self.search_wid.setHidden(True)                 # 查询界面隐藏
        self.edit_wid.setHidden(True)                   # 隐藏增加，删除按键窗口

        # 设置水平布局盒子，并命名为horizontalLayout3
        self.horizontalLayout3 = QtWidgets.QHBoxLayout(self.Web_wid)
        self.horizontalLayout3.setObjectName("horizontalLayout3")
        self.horizontalLayout3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout3.setSpacing(0)
        # 手动创建QWebEngineView 控件
        self.qwebengine = QWebEngineView()
        self.qwebengine.setParent(self.Web_wid)
        # 往Bottom 窗口添加 QWebEngineView 控件，并实现水平布局
        self.horizontalLayout3.addWidget(self.qwebengine)
        QWebEngineProfile.defaultProfile().setHttpUserAgent('Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36 TheWorld 6')
        # 清除COOKIE
        QWebEngineProfile.defaultProfile().cookieStore().deleteAllCookies()
        # 设置隐藏
        self.Web_wid.setHidden(True)
        # 子控件添加事件处理，必须语句
        self.Top_wid.installEventFilter(self)

    def eventFilter(self, objwatched, event):                   # 设置事件过滤函数
        eventType = event.type()
        if objwatched == self.Top_wid:
            if eventType == QEvent.Enter:                       # 鼠标进入窗体内部
                if not self.taskList_btn.isChecked():
                    self.setTopexpand(0, 0)                     # 动画，将窗口弹出20
                    self.setWebexpand(0,25)
            elif eventType == QEvent.Leave:                     # 鼠标离开窗体
                if not self.taskList_btn.isChecked():
                    self.setTopexpand(0, -20)                   # 动画，将窗口收回20
                    self.setWebexpand(0,2)
                pass
            elif eventType == QEvent.MouseButtonPress:          # 鼠标在Top_wid单击，计算出窗口偏移坐标
                self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
                QApplication.postEvent(self, QEvent(174))
                event.accept()
            elif eventType == QEvent.MouseMove:                 # 鼠标挪动，将窗口移动
                try:
                    self.move(event.globalPos() - self.dragPosition)
                    event.accept()
                except:pass
        return super().eventFilter(objwatched, event)

    def setTopexpand(self,x,y):                      # 动画函数
        # 为Top_wid 设置动画，并且动画小姑为平推
        animation = QPropertyAnimation(self.Top_wid,b"geometry",self)
        # 创建一个新的动画样式
        startpos = self.Top_wid.geometry()
        # 设置动画时长
        animation.setDuration(500)
        # 设置移动后位置
        newpos = QRect(x,y,startpos.width(),25)
        animation.setEndValue(newpos)
        # 执行动画
        animation.start()

    def setWebexpand(self,x,y):                      # 动画函数
        # 为Top_wid 设置动画，并且动画小姑为平推
        animation = QPropertyAnimation(self.Web_wid,b"geometry",self)
        # 创建一个新的动画样式
        startpos = self.Web_wid
        # 设置动画时长
        animation.setDuration(500)
        # 设置移动后位置
        newpos = QRect(x,y,startpos.width(),startpos.height())
        animation.setEndValue(newpos)
        # 执行动画
        animation.start()

    # Top_wid 按键被点击
    def listChoose_comb_change(self):
        if self.taskList_btn.isChecked():
            if self.taskInformation_btn.isChecked() and not self.waring_btn.isChecked():  # 查看电子流信息
                self.listChoose_comb_change_signal.emit(self.webtext,self.listChoose_comb.currentText())

    def newForm_btn_click(self,checked):

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

    # Left_wid 按键被点击
    def taskInformation_btn_click(self,checked):                # 订单信息按钮按下
        if checked :
            self.tableView_Top_wid.setHidden(False)             # 打开listChoose等
            self.listChoose_comb.setEnabled(True)               # 设置生产指示单下拉框打开
            self.waring_btn.setChecked(False)                   # 设置其他按钮关闭
            self.pcbInformation_btn.setChecked(False)           # 设置其他按钮关闭
            self.search_wid.setHidden(True)                     # 设置料号查询窗口关闭
            self.edit_wid.setHidden(True)                       # 设置add，del按键隐藏
            self.refreshWebtext()
        else:
            self.listChoose_comb.setEnabled(False)              # 设置生产指示单下拉框禁止
            self.taskInformation_btn.setChecked(True)

    def waring_btn_click(self,checked):                         # 订单注意事项按钮按下
        if checked:
            self.search_wid.setHidden(False)                   # 打开料号查询窗口
            self.tableView_Top_wid.setHidden(True)              # 订单查询窗口关闭
            self.listChoose_comb.setEnabled(False)              # 设置生产指示单下拉框禁止
            self.taskInformation_btn.setChecked(False)          # 设置订单信息按钮关闭
            self.pcbInformation_btn.setChecked(False)           # 设置PCB未下订单按钮关闭
            self.edit_wid.setHidden(False)                       # 设置add，del按键隐藏
            self.waring_btn_click_signal.emit()
        else:
            self.search_wid.setHidden(True)

    def pcbInformation_btn_click(self,checked):
        if checked:
            self.search_wid.setHidden(True)                   # 关闭料号查询窗口
            self.tableView_Top_wid.setHidden(True)              # 关闭订单查询窗口
            self.listChoose_comb.setEnabled(False)              # 设置生产指示单下拉框禁止
            self.taskInformation_btn.setChecked(False)          # 设置订单信息按钮关闭
            self.waring_btn.setChecked(False)           # 设置PCB未下订单按钮关闭
        else:
            self.pcbInformation_btn.setChecked(True)

    # search_wid 查询按钮被点击
    def search_btn_click(self):
        self.search_btn_click_signal.emit(self.projectName_Ledit.text(),self.projectNum_Ledit.text(),self.projectSpec_Ledit.text(),'WaringInformation')

    def add_btn_click(self):
        self.add_btn_click_signal.emit(self.projectName_Ledit.text(),self.projectNum_Ledit.text(),self.projectSpec_Ledit.text())

    def del_btn_click(self):
        #TODO 优化3 删除当前选中的数据
        selectIndex = self.display_tab.selectionModel().selectedIndexes()
        selectRow = []
        delList = []
        # QmodelIndex数据转成int，换得到相应的row
        for index in selectIndex:
            if index.column() == 0:
                delNum = str(self.display_tab.model.index(index.row(),1).data()).strip()
                delList.append(delNum)
                selectRow.append(index.row())
        selectRow.reverse()
        if len(selectRow)>0:
            for row in selectRow:
                self.display_tab.model.removeRows(row,1)
        # 发送信号，处理pandas 数据，操作excel
        self.del_btn_click_signal.emit(delList)

    # 电子流类型框被选择
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

    def displayTablelist(self,displayList,head):

        if len(displayList) != 0:
            rows = displayList.shape[0]              # 行计算
            colums = displayList.shape[1]            # 列计算
            # 编辑待处理任务数量
            self.displayPro_labe.setText('待处理任务:[%s/%s]' % (rows,rows))
            # 设置表格内容不能被修改
            #self.display_tab.setEditTriggers(QAbstractItemView.NoEditTriggers0No)
            # 设置表格选择方式，整行选择
            self.display_tab.setSelectionBehavior(1)
            # 设置表格不带边框
            self.display_tab.setShowGrid(False)
            # 设置数据层次结构，m行n列
            self.display_tab.model = QStandardItemModel(rows, colums)
            # 设置水平方向四个头标签文本内容
            self.display_tab.model.setHorizontalHeaderLabels(head)

            # Todo 优化2 添加数据
            # self.model.appendRow([
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            #     QStandardItem('row %s,column %s' % (11,11)),
            # ])

            for row in range(rows):
                for column in range(colums):
                    if column != colums-1:                                      # 针对异常工艺反馈表，删除最后一列简短描述
                        item = QStandardItem(" "*4 + str(displayList[row][column]) + " "*4)                  # 显示内容增加空格，美观
                    else:
                        # str。find 函数，如果未找到字符串返回-1，找到了返回子字符串index
                        if str(displayList[row][column]).find("简短描述：") != -1:
                            text = str(displayList[row][column]).replace("简短描述：","")
                            item = QStandardItem(text)
                        else:
                            item = QStandardItem(displayList[row][column])
                    # 设置每个位置的文本值
                    self.display_tab.model.setItem(row, column, item)

            self.display_tab.setModel(self.display_tab.model)

            #todo 优化1 表格填满窗口
            #水平方向标签拓展剩下的窗口部分，填满表格
            self.display_tab.horizontalHeader().setStretchLastSection(True)
            #水平方向，表格大小拓展到适当的尺寸
            self.display_tab.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

            for column in range(colums):
                # 每列根据内容设置
                self.display_tab.horizontalHeader().setSectionResizeMode(column,QHeaderView.ResizeToContents)

            for row in range(rows):
                # 随内容分配行高
                self.display_tab.verticalHeader().setSectionResizeMode(row, QHeaderView.ResizeToContents)

        else:
            self.display_tab.model = QStandardItemModel(0, 0)
            self.display_tab.setModel(self.display_tab.model)

    def inverse_rad_checked(self):
        # 获取当前选中的行 QmodelIndex
        selectIndex = self.display_tab.selectionModel().selectedIndexes()
        selectRow = []
        inverseRow = []
        # QmodelIndex数据转成int，换得到相应的row
        for index in selectIndex:
            if index.column() == 0:
                selectRow.append(index.row())
        # 清除选中的行，准备重新选择
        self.display_tab.clearSelection()
        # 获取当前tableview数据的行数
        # 注意语法：self.display_tab.model().rowCount()会报错（model多了括号），但是C++又需要带括号
        indexCount = self.display_tab.model.rowCount()
        # 得到取反的行号
        for i in range(indexCount):
            if i not in selectRow:
                inverseRow.append(i)
        # 数据转换，将int转化成QmodelIndex
        indexes = [self.display_tab.model.index(r, 0) for r in inverseRow]
        # 设置选中模式
        mode = QtCore.QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
        # 最终选中，实现反选
        [self.display_tab.selectionModel().select(index, mode) for index in indexes]

    def refreshWebtext(self):
        self.refreshWebtext_signal.emit()
