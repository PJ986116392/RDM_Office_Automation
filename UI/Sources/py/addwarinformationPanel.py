from UI.Sources.ui.addwarInformation_UI import Ui_Form
from PyQt5.Qt import *
from PyQt5 import QtWidgets,QtCore

class Addwarinf(QWidget,Ui_Form):
    addwindow_search_btn_click_signal = pyqtSignal(str, str, str,str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 点击右上角叉，不关闭进程，只是关闭当前窗口
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        # 新建的窗口始终位于当前屏幕的最前面
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # 阻塞父类窗口不能点击
        self.setWindowModality(Qt.ApplicationModal)

    # search_wid 查询按钮被点击
    def search_btn_click(self):
        self.addwindow_search_btn_click_signal.emit(self.projectName_Ledit.text(),self.projectNum_Ledit.text(),self.projectSpec_Ledit.text(),'addWindow')

    def inverse_rad_checked(self):
        selectIndex = self.display_tab.selectionModel().selectedIndexes()
        self.display_tab.selectionModel().clear()
        mode = QtCore.QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
        for index in self.display_tab.model().index():
            if index not in selectIndex:
                self.display_tab.selectionModel().select(index, mode)

        # rows = [1, 2, 3]
        # indexes = [self.display_tab.model.index(r, 0) for r in rows]
        # mode = QtCore.QItemSelectionModel.Select | QtCore.QItemSelectionModel.Rows
        # [self.display_tab.selectionModel().select(index, mode) for index in indexes]

    def displayTablelist(self,displayList,head):
        if len(displayList) != 0:
            rows = displayList.shape[0]              # 行计算
            colums = displayList.shape[1]            # 列计算

            # 设置表格选择方式，整行选择
            self.display_tab.setSelectionBehavior(1)
            # 设置表格不带边框
            self.display_tab.setShowGrid(False)
            # 设置数据层次结构，m行n列
            self.display_tab.model = QStandardItemModel(rows, colums)
            # 设置水平方向四个头标签文本内容
            self.display_tab.model.setHorizontalHeaderLabels(head)

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

            # #TODO 优化3 删除当前选中的数据
            # indexs=self.display_tab.selectionModel().selection().indexes()
            # print(indexs)
            # if len(indexs)>0:
            #     index=indexs[0]
            #     self.model.removeRows(index.row(),1)
        else:
            self.display_tab.model = QStandardItemModel(0, 0)
            self.display_tab.setModel(self.display_tab.model)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Addwarinf()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())