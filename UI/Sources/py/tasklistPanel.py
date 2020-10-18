from UI.Sources.ui.taskList_UI import Ui_TaskListWindow
from PyQt5.Qt import *
class TaskList(QWidget,Ui_TaskListWindow):

    listChoose_comb_change_signal = pyqtSignal(str,str)
    refreshWebtext_signal = pyqtSignal()

    def __init__(self,webtext,displayList):
        super().__init__()
        self.webtext = webtext
        self.displayList = displayList
        self.setupUi(self)
        self.taskList_btn.setChecked(True)              # 设置待处理任务按钮选中
        self.btn_checkFalse('taskList_btn')             # 设置填写新表单等按钮取消
        self.taskInformation_btn.setChecked(True)       # 设置订单信息按钮选中
        self.waring_btn.setChecked(False)               # 设置注意事项按钮取消
        self.add_btn.setHidden(True)                    # 设置注意事项增加按钮隐藏
        self.delete_btn.setHidden(True)                 # 设置注意事项增加按钮隐藏

    def listChoose_comb_change(self):
        if self.taskList_btn.isChecked():
            if self.taskInformation_btn.isChecked() and not self.waring_btn.isChecked():  # 查看电子流信息
                text = self.listChoose_comb.currentText()
                self.listChoose_comb_change_signal.emit(self.webtext,text)

    def newForm_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('newForm_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

    def draft_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('draft_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

    def taskList_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            # 界面互动
            self.btn_checkFalse('taskList_btn')
            #self.showMinimized()
            self.widget_4.setHidden(False)
            self.widget_5.setHidden(False)

    def historicalSen_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('historicalSen_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

    def historicalPro_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('historicalPro_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

    def Form_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('Form_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

    def lookFor_btn_click(self,checked):
        if checked:                                     # 其他按钮取消
            self.btn_checkFalse('lookFor_btn')
            #self.showMinimized()
            self.widget_4.setHidden(True)
            self.widget_5.setHidden(True)

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
        widget = self.widget

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


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    list =  [['PO20191129001','生产指示单','刘博鹏由王冬琴代填','2019-11-29 09:52:23','TV电源硬件','制单人:王冬琴,客户代码：C058受订单号：SO191129001,品号:601E628H01TV13002L','1235553','85525']]

    window = TaskList(list)
    window.show()
    sys.exit(app.exec_())