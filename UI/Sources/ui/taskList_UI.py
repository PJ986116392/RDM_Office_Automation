# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Project_Python\RDM_Office_Automation\UI\Sources\ui\taskList_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskListWindow(object):
    def setupUi(self, TaskListWindow):
        TaskListWindow.setObjectName("TaskListWindow")
        TaskListWindow.resize(1200, 900)
        TaskListWindow.setMinimumSize(QtCore.QSize(1200, 900))
        TaskListWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        TaskListWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(TaskListWindow)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Top_wid = QtWidgets.QWidget(TaskListWindow)
        self.Top_wid.setObjectName("Top_wid")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_wid)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.newForm_btn = QtWidgets.QPushButton(self.Top_wid)
        self.newForm_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.newForm_btn.setCheckable(True)
        self.newForm_btn.setFlat(True)
        self.newForm_btn.setObjectName("newForm_btn")
        self.horizontalLayout.addWidget(self.newForm_btn)
        self.draft_btn = QtWidgets.QPushButton(self.Top_wid)
        self.draft_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.draft_btn.setCheckable(True)
        self.draft_btn.setFlat(True)
        self.draft_btn.setObjectName("draft_btn")
        self.horizontalLayout.addWidget(self.draft_btn)
        self.taskList_btn = QtWidgets.QPushButton(self.Top_wid)
        self.taskList_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.taskList_btn.setCheckable(True)
        self.taskList_btn.setChecked(False)
        self.taskList_btn.setDefault(False)
        self.taskList_btn.setFlat(True)
        self.taskList_btn.setObjectName("taskList_btn")
        self.horizontalLayout.addWidget(self.taskList_btn)
        self.historicalSen_btn = QtWidgets.QPushButton(self.Top_wid)
        self.historicalSen_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.historicalSen_btn.setCheckable(True)
        self.historicalSen_btn.setFlat(True)
        self.historicalSen_btn.setObjectName("historicalSen_btn")
        self.horizontalLayout.addWidget(self.historicalSen_btn)
        self.historicalPro_btn = QtWidgets.QPushButton(self.Top_wid)
        self.historicalPro_btn.setStyleSheet("")
        self.historicalPro_btn.setCheckable(True)
        self.historicalPro_btn.setFlat(True)
        self.historicalPro_btn.setObjectName("historicalPro_btn")
        self.horizontalLayout.addWidget(self.historicalPro_btn)
        self.lookFor_btn = QtWidgets.QPushButton(self.Top_wid)
        self.lookFor_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.lookFor_btn.setCheckable(True)
        self.lookFor_btn.setFlat(True)
        self.lookFor_btn.setObjectName("lookFor_btn")
        self.horizontalLayout.addWidget(self.lookFor_btn)
        self.Form_btn = QtWidgets.QPushButton(self.Top_wid)
        self.Form_btn.setStyleSheet("fontcolor:rgb(0, 170, 255)")
        self.Form_btn.setCheckable(True)
        self.Form_btn.setFlat(True)
        self.Form_btn.setObjectName("Form_btn")
        self.horizontalLayout.addWidget(self.Form_btn)
        spacerItem = QtWidgets.QSpacerItem(612, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.Top_wid, 0, 0, 1, 2)
        self.Left_wid = QtWidgets.QWidget(TaskListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Left_wid.sizePolicy().hasHeightForWidth())
        self.Left_wid.setSizePolicy(sizePolicy)
        self.Left_wid.setMinimumSize(QtCore.QSize(25, 0))
        self.Left_wid.setMaximumSize(QtCore.QSize(25, 16777215))
        self.Left_wid.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.Left_wid.setObjectName("Left_wid")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Left_wid)
        self.verticalLayout.setContentsMargins(0, 0, 0, 600)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.taskInformation_btn = QtWidgets.QPushButton(self.Left_wid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.taskInformation_btn.sizePolicy().hasHeightForWidth())
        self.taskInformation_btn.setSizePolicy(sizePolicy)
        self.taskInformation_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.taskInformation_btn.setCheckable(True)
        self.taskInformation_btn.setChecked(False)
        self.taskInformation_btn.setFlat(True)
        self.taskInformation_btn.setObjectName("taskInformation_btn")
        self.verticalLayout.addWidget(self.taskInformation_btn)
        self.waring_btn = QtWidgets.QPushButton(self.Left_wid)
        self.waring_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.waring_btn.setCheckable(True)
        self.waring_btn.setFlat(True)
        self.waring_btn.setObjectName("waring_btn")
        self.verticalLayout.addWidget(self.waring_btn)
        self.verticalLayout.setStretch(1, 2)
        self.gridLayout.addWidget(self.Left_wid, 1, 0, 1, 1)
        self.Table_veiw_wid = QtWidgets.QWidget(TaskListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_veiw_wid.sizePolicy().hasHeightForWidth())
        self.Table_veiw_wid.setSizePolicy(sizePolicy)
        self.Table_veiw_wid.setStyleSheet("")
        self.Table_veiw_wid.setObjectName("Table_veiw_wid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Table_veiw_wid)
        self.gridLayout_2.setContentsMargins(0, 10, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.add_btn = QtWidgets.QPushButton(self.Table_veiw_wid)
        self.add_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.add_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.add_btn.setObjectName("add_btn")
        self.gridLayout_2.addWidget(self.add_btn, 2, 5, 1, 1, QtCore.Qt.AlignRight)
        self.object_choose_comb = QtWidgets.QComboBox(self.Table_veiw_wid)
        self.object_choose_comb.setMinimumSize(QtCore.QSize(150, 25))
        self.object_choose_comb.setMaximumSize(QtCore.QSize(150, 25))
        self.object_choose_comb.setEditable(True)
        self.object_choose_comb.setObjectName("object_choose_comb")
        self.gridLayout_2.addWidget(self.object_choose_comb, 0, 3, 1, 1)
        self.search_btn = QtWidgets.QPushButton(self.Table_veiw_wid)
        self.search_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_btn.setFlat(True)
        self.search_btn.setObjectName("search_btn")
        self.gridLayout_2.addWidget(self.search_btn, 0, 4, 1, 1)
        self.listChoose_comb = QtWidgets.QComboBox(self.Table_veiw_wid)
        self.listChoose_comb.setEnabled(True)
        self.listChoose_comb.setMinimumSize(QtCore.QSize(150, 25))
        self.listChoose_comb.setMaximumSize(QtCore.QSize(150, 25))
        self.listChoose_comb.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.listChoose_comb.setEditable(False)
        self.listChoose_comb.setObjectName("listChoose_comb")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.listChoose_comb.addItem("")
        self.gridLayout_2.addWidget(self.listChoose_comb, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 5, 1, 1)
        self.delete_btn = QtWidgets.QPushButton(self.Table_veiw_wid)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMinimumSize(QtCore.QSize(25, 25))
        self.delete_btn.setMaximumSize(QtCore.QSize(25, 25))
        self.delete_btn.setObjectName("delete_btn")
        self.gridLayout_2.addWidget(self.delete_btn, 3, 5, 1, 1, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(671, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        self.displayPro_labe = QtWidgets.QLabel(self.Table_veiw_wid)
        self.displayPro_labe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.displayPro_labe.setObjectName("displayPro_labe")
        self.gridLayout_2.addWidget(self.displayPro_labe, 0, 0, 1, 1)
        self.tableView = QtWidgets.QTableView(self.Table_veiw_wid)
        self.tableView.setMinimumSize(QtCore.QSize(1150, 0))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setWordWrap(True)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 1, 0, 4, 5)
        self.gridLayout.addWidget(self.Table_veiw_wid, 1, 1, 1, 1)
        self.Waring_wid = QtWidgets.QWidget(TaskListWindow)
        self.Waring_wid.setObjectName("Waring_wid")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Waring_wid)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.waring_labe = QtWidgets.QLabel(self.Waring_wid)
        self.waring_labe.setEnabled(False)
        self.waring_labe.setObjectName("waring_labe")
        self.horizontalLayout_2.addWidget(self.waring_labe, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.Waring_wid, 3, 0, 1, 2, QtCore.Qt.AlignBottom)
        self.Web_wid = QtWidgets.QWidget(TaskListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Web_wid.sizePolicy().hasHeightForWidth())
        self.Web_wid.setSizePolicy(sizePolicy)
        self.Web_wid.setMinimumSize(QtCore.QSize(1200, 0))
        self.Web_wid.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Web_wid.setStyleSheet("")
        self.Web_wid.setObjectName("Web_wid")
        self.gridLayout.addWidget(self.Web_wid, 2, 0, 1, 2)

        self.retranslateUi(TaskListWindow)
        self.newForm_btn.clicked['bool'].connect(TaskListWindow.newForm_btn_click)
        self.draft_btn.clicked['bool'].connect(TaskListWindow.draft_btn_click)
        self.taskList_btn.clicked['bool'].connect(TaskListWindow.taskList_btn_click)
        self.historicalSen_btn.clicked['bool'].connect(TaskListWindow.historicalSen_btn_click)
        self.historicalPro_btn.clicked['bool'].connect(TaskListWindow.historicalPro_btn_click)
        self.Form_btn.clicked['bool'].connect(TaskListWindow.Form_btn_click)
        self.lookFor_btn.clicked['bool'].connect(TaskListWindow.lookFor_btn_click)
        self.taskInformation_btn.clicked['bool'].connect(TaskListWindow.taskInformation_btn_click)
        self.waring_btn.clicked['bool'].connect(TaskListWindow.waring_btn_click)
        self.listChoose_comb.currentTextChanged['QString'].connect(TaskListWindow.listChoose_comb_change)
        self.search_btn.clicked.connect(TaskListWindow.refreshWebtext)
        QtCore.QMetaObject.connectSlotsByName(TaskListWindow)

    def retranslateUi(self, TaskListWindow):
        _translate = QtCore.QCoreApplication.translate
        TaskListWindow.setWindowTitle(_translate("TaskListWindow", "Form"))
        self.newForm_btn.setText(_translate("TaskListWindow", "填写新表单"))
        self.draft_btn.setText(_translate("TaskListWindow", "草稿"))
        self.taskList_btn.setText(_translate("TaskListWindow", "待处理任务"))
        self.historicalSen_btn.setText(_translate("TaskListWindow", "历史申请"))
        self.historicalPro_btn.setText(_translate("TaskListWindow", "历史处理"))
        self.lookFor_btn.setText(_translate("TaskListWindow", "业务查询"))
        self.Form_btn.setText(_translate("TaskListWindow", "报表"))
        self.taskInformation_btn.setText(_translate("TaskListWindow", "订\n"
"单\n"
"信\n"
"息"))
        self.waring_btn.setText(_translate("TaskListWindow", "注\n"
"意\n"
"事\n"
"项"))
        self.add_btn.setText(_translate("TaskListWindow", "+"))
        self.search_btn.setText(_translate("TaskListWindow", "Search"))
        self.listChoose_comb.setItemText(0, _translate("TaskListWindow", "生产指示单"))
        self.listChoose_comb.setItemText(1, _translate("TaskListWindow", "成品料号申请表"))
        self.listChoose_comb.setItemText(2, _translate("TaskListWindow", "BOM制作指导单"))
        self.listChoose_comb.setItemText(3, _translate("TaskListWindow", "(新)ECN变更申请单"))
        self.listChoose_comb.setItemText(4, _translate("TaskListWindow", "生产通知单"))
        self.listChoose_comb.setItemText(5, _translate("TaskListWindow", "PCB料号申请单"))
        self.listChoose_comb.setItemText(6, _translate("TaskListWindow", "异常工艺反馈改善表"))
        self.listChoose_comb.setItemText(7, _translate("TaskListWindow", "成品料号申请表"))
        self.listChoose_comb.setItemText(8, _translate("TaskListWindow", "料号申请表(2018)"))
        self.delete_btn.setText(_translate("TaskListWindow", "-"))
        self.displayPro_labe.setText(_translate("TaskListWindow", "待处理任务:[7/7]"))
        self.waring_labe.setText(_translate("TaskListWindow", "状态栏:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskListWindow = QtWidgets.QWidget()
    ui = Ui_TaskListWindow()
    ui.setupUi(TaskListWindow)
    TaskListWindow.show()
    sys.exit(app.exec_())