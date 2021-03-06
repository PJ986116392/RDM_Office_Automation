# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'taskList_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TaskListWindow(object):
    def setupUi(self, TaskListWindow):
        TaskListWindow.setObjectName("TaskListWindow")
        TaskListWindow.resize(1362, 866)
        TaskListWindow.setMinimumSize(QtCore.QSize(1200, 100))
        TaskListWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        TaskListWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.gridLayout = QtWidgets.QGridLayout(TaskListWindow)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.Table_veiw_wid = QtWidgets.QWidget(TaskListWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Table_veiw_wid.sizePolicy().hasHeightForWidth())
        self.Table_veiw_wid.setSizePolicy(sizePolicy)
        self.Table_veiw_wid.setStyleSheet("")
        self.Table_veiw_wid.setObjectName("Table_veiw_wid")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Table_veiw_wid)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableView_Top_wid = QtWidgets.QWidget(self.Table_veiw_wid)
        self.tableView_Top_wid.setMinimumSize(QtCore.QSize(0, 30))
        self.tableView_Top_wid.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tableView_Top_wid.setObjectName("tableView_Top_wid")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tableView_Top_wid)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.displayPro_labe = QtWidgets.QLabel(self.tableView_Top_wid)
        self.displayPro_labe.setMinimumSize(QtCore.QSize(0, 25))
        self.displayPro_labe.setMaximumSize(QtCore.QSize(16777215, 25))
        self.displayPro_labe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.displayPro_labe.setObjectName("displayPro_labe")
        self.horizontalLayout_3.addWidget(self.displayPro_labe)
        spacerItem = QtWidgets.QSpacerItem(701, 9, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.listChoose_comb = QtWidgets.QComboBox(self.tableView_Top_wid)
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
        self.horizontalLayout_3.addWidget(self.listChoose_comb)
        self.new_btn = QtWidgets.QPushButton(self.tableView_Top_wid)
        self.new_btn.setMinimumSize(QtCore.QSize(0, 25))
        self.new_btn.setMaximumSize(QtCore.QSize(16777215, 25))
        self.new_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.new_btn.setFlat(True)
        self.new_btn.setObjectName("new_btn")
        self.horizontalLayout_3.addWidget(self.new_btn)
        self.gridLayout_2.addWidget(self.tableView_Top_wid, 0, 0, 1, 2)
        self.search_wid = QtWidgets.QWidget(self.Table_veiw_wid)
        self.search_wid.setMinimumSize(QtCore.QSize(0, 30))
        self.search_wid.setMaximumSize(QtCore.QSize(16777215, 20))
        self.search_wid.setObjectName("search_wid")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.search_wid)
        self.horizontalLayout_4.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.search_wid)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.projectName_Ledit = QtWidgets.QLineEdit(self.search_wid)
        self.projectName_Ledit.setMinimumSize(QtCore.QSize(0, 25))
        self.projectName_Ledit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.projectName_Ledit.setObjectName("projectName_Ledit")
        self.horizontalLayout_4.addWidget(self.projectName_Ledit)
        self.label_2 = QtWidgets.QLabel(self.search_wid)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.projectNum_Ledit = QtWidgets.QLineEdit(self.search_wid)
        self.projectNum_Ledit.setMinimumSize(QtCore.QSize(0, 25))
        self.projectNum_Ledit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.projectNum_Ledit.setObjectName("projectNum_Ledit")
        self.horizontalLayout_4.addWidget(self.projectNum_Ledit)
        self.label_3 = QtWidgets.QLabel(self.search_wid)
        self.label_3.setMinimumSize(QtCore.QSize(0, 25))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.projectSpec_Ledit = QtWidgets.QLineEdit(self.search_wid)
        self.projectSpec_Ledit.setMinimumSize(QtCore.QSize(0, 25))
        self.projectSpec_Ledit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.projectSpec_Ledit.setObjectName("projectSpec_Ledit")
        self.horizontalLayout_4.addWidget(self.projectSpec_Ledit)
        self.search_btn = QtWidgets.QPushButton(self.search_wid)
        self.search_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.search_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.allChoose_Rad = QtWidgets.QRadioButton(self.search_wid)
        self.allChoose_Rad.setEnabled(False)
        self.allChoose_Rad.setMinimumSize(QtCore.QSize(0, 25))
        self.allChoose_Rad.setMaximumSize(QtCore.QSize(16777215, 25))
        self.allChoose_Rad.setObjectName("allChoose_Rad")
        self.horizontalLayout_4.addWidget(self.allChoose_Rad)
        self.inverse_Rad = QtWidgets.QRadioButton(self.search_wid)
        self.inverse_Rad.setEnabled(False)
        self.inverse_Rad.setMinimumSize(QtCore.QSize(0, 25))
        self.inverse_Rad.setMaximumSize(QtCore.QSize(16777215, 25))
        self.inverse_Rad.setObjectName("inverse_Rad")
        self.horizontalLayout_4.addWidget(self.inverse_Rad)
        self.gridLayout_2.addWidget(self.search_wid, 1, 0, 1, 2)
        self.display_tab = QtWidgets.QTableView(self.Table_veiw_wid)
        self.display_tab.setMinimumSize(QtCore.QSize(0, 0))
        self.display_tab.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.display_tab.setToolTip("")
        self.display_tab.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.display_tab.setWordWrap(True)
        self.display_tab.setObjectName("display_tab")
        self.gridLayout_2.addWidget(self.display_tab, 2, 0, 1, 1)
        self.edit_wid = QtWidgets.QWidget(self.Table_veiw_wid)
        self.edit_wid.setMinimumSize(QtCore.QSize(0, 0))
        self.edit_wid.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edit_wid.setObjectName("edit_wid")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.edit_wid)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_btn = QtWidgets.QPushButton(self.edit_wid)
        self.add_btn.setEnabled(False)
        self.add_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.add_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_btn.setCheckable(False)
        self.add_btn.setAutoDefault(False)
        self.add_btn.setDefault(False)
        self.add_btn.setFlat(True)
        self.add_btn.setObjectName("add_btn")
        self.verticalLayout_2.addWidget(self.add_btn)
        self.del_btn = QtWidgets.QPushButton(self.edit_wid)
        self.del_btn.setEnabled(False)
        self.del_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.del_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.del_btn.setCheckable(False)
        self.del_btn.setAutoDefault(False)
        self.del_btn.setFlat(True)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout_2.addWidget(self.del_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 630, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.edit_wid, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.Table_veiw_wid, 1, 1, 1, 1)
        self.Top_wid = QtWidgets.QWidget(TaskListWindow)
        self.Top_wid.setMinimumSize(QtCore.QSize(0, 30))
        self.Top_wid.setMaximumSize(QtCore.QSize(16777215, 30))
        self.Top_wid.setObjectName("Top_wid")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_wid)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 5)
        self.horizontalLayout.setSpacing(0)
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
        spacerItem2 = QtWidgets.QSpacerItem(612, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addWidget(self.Top_wid, 0, 0, 1, 3)
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
        self.gridLayout.addWidget(self.Web_wid, 2, 0, 1, 3)
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
        self.verticalLayout.setContentsMargins(0, 30, 0, 0)
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
        self.pcbInformation_btn = QtWidgets.QPushButton(self.Left_wid)
        self.pcbInformation_btn.setMaximumSize(QtCore.QSize(25, 16777215))
        self.pcbInformation_btn.setCheckable(True)
        self.pcbInformation_btn.setFlat(True)
        self.pcbInformation_btn.setObjectName("pcbInformation_btn")
        self.verticalLayout.addWidget(self.pcbInformation_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 439, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addWidget(self.Left_wid, 1, 0, 1, 1)
        self.Waring_wid = QtWidgets.QWidget(TaskListWindow)
        self.Waring_wid.setMinimumSize(QtCore.QSize(0, 40))
        self.Waring_wid.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Waring_wid.setObjectName("Waring_wid")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Waring_wid)
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.waring_labe = QtWidgets.QLabel(self.Waring_wid)
        self.waring_labe.setEnabled(False)
        self.waring_labe.setObjectName("waring_labe")
        self.horizontalLayout_2.addWidget(self.waring_labe)
        self.combit_rad = QtWidgets.QRadioButton(self.Waring_wid)
        self.combit_rad.setMaximumSize(QtCore.QSize(60, 30))
        self.combit_rad.setChecked(True)
        self.combit_rad.setObjectName("combit_rad")
        self.horizontalLayout_2.addWidget(self.combit_rad)
        self.comeback_rad = QtWidgets.QRadioButton(self.Waring_wid)
        self.comeback_rad.setMaximumSize(QtCore.QSize(60, 30))
        self.comeback_rad.setObjectName("comeback_rad")
        self.horizontalLayout_2.addWidget(self.comeback_rad)
        self.comback_comb = QtWidgets.QComboBox(self.Waring_wid)
        self.comback_comb.setEnabled(False)
        self.comback_comb.setMaximumSize(QtCore.QSize(150, 30))
        self.comback_comb.setObjectName("comback_comb")
        self.comback_comb.addItem("")
        self.horizontalLayout_2.addWidget(self.comback_comb)
        self.taskCombit_btn = QtWidgets.QPushButton(self.Waring_wid)
        self.taskCombit_btn.setEnabled(True)
        self.taskCombit_btn.setMinimumSize(QtCore.QSize(50, 0))
        self.taskCombit_btn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.taskCombit_btn.setObjectName("taskCombit_btn")
        self.horizontalLayout_2.addWidget(self.taskCombit_btn)
        self.gridLayout.addWidget(self.Waring_wid, 3, 0, 1, 3)

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
        self.new_btn.clicked.connect(TaskListWindow.refreshWebtext)
        self.pcbInformation_btn.clicked['bool'].connect(TaskListWindow.pcbInformation_btn_click)
        self.search_btn.clicked.connect(TaskListWindow.search_btn_click)
        self.add_btn.clicked.connect(TaskListWindow.add_btn_click)
        self.del_btn.clicked.connect(TaskListWindow.del_btn_click)
        self.allChoose_Rad.clicked.connect(self.display_tab.selectAll)
        self.inverse_Rad.clicked.connect(TaskListWindow.inverse_rad_checked)
        self.combit_rad.clicked['bool'].connect(TaskListWindow.combit_rad_checked)
        self.comeback_rad.clicked['bool'].connect(TaskListWindow.comeback_rad_checked)
        self.taskCombit_btn.clicked.connect(TaskListWindow.combit_btn_click)
        QtCore.QMetaObject.connectSlotsByName(TaskListWindow)
        TaskListWindow.setTabOrder(self.newForm_btn, self.draft_btn)
        TaskListWindow.setTabOrder(self.draft_btn, self.taskList_btn)
        TaskListWindow.setTabOrder(self.taskList_btn, self.historicalSen_btn)
        TaskListWindow.setTabOrder(self.historicalSen_btn, self.historicalPro_btn)
        TaskListWindow.setTabOrder(self.historicalPro_btn, self.lookFor_btn)
        TaskListWindow.setTabOrder(self.lookFor_btn, self.Form_btn)
        TaskListWindow.setTabOrder(self.Form_btn, self.taskInformation_btn)
        TaskListWindow.setTabOrder(self.taskInformation_btn, self.waring_btn)
        TaskListWindow.setTabOrder(self.waring_btn, self.pcbInformation_btn)
        TaskListWindow.setTabOrder(self.pcbInformation_btn, self.listChoose_comb)
        TaskListWindow.setTabOrder(self.listChoose_comb, self.new_btn)
        TaskListWindow.setTabOrder(self.new_btn, self.projectName_Ledit)
        TaskListWindow.setTabOrder(self.projectName_Ledit, self.projectNum_Ledit)
        TaskListWindow.setTabOrder(self.projectNum_Ledit, self.projectSpec_Ledit)
        TaskListWindow.setTabOrder(self.projectSpec_Ledit, self.search_btn)
        TaskListWindow.setTabOrder(self.search_btn, self.allChoose_Rad)
        TaskListWindow.setTabOrder(self.allChoose_Rad, self.inverse_Rad)
        TaskListWindow.setTabOrder(self.inverse_Rad, self.display_tab)
        TaskListWindow.setTabOrder(self.display_tab, self.add_btn)
        TaskListWindow.setTabOrder(self.add_btn, self.del_btn)

    def retranslateUi(self, TaskListWindow):
        _translate = QtCore.QCoreApplication.translate
        TaskListWindow.setWindowTitle(_translate("TaskListWindow", "Form"))
        self.displayPro_labe.setText(_translate("TaskListWindow", "待处理任务:"))
        self.listChoose_comb.setItemText(0, _translate("TaskListWindow", "生产指示单"))
        self.listChoose_comb.setItemText(1, _translate("TaskListWindow", "成品料号申请表"))
        self.listChoose_comb.setItemText(2, _translate("TaskListWindow", "BOM制作指导单"))
        self.listChoose_comb.setItemText(3, _translate("TaskListWindow", "(新)ECN变更申请单"))
        self.listChoose_comb.setItemText(4, _translate("TaskListWindow", "生产通知单"))
        self.listChoose_comb.setItemText(5, _translate("TaskListWindow", "PCB料号申请单"))
        self.listChoose_comb.setItemText(6, _translate("TaskListWindow", "异常工艺反馈改善表"))
        self.listChoose_comb.setItemText(7, _translate("TaskListWindow", "成品料号申请表"))
        self.listChoose_comb.setItemText(8, _translate("TaskListWindow", "料号申请表(2018)"))
        self.new_btn.setText(_translate("TaskListWindow", "刷新"))
        self.label.setText(_translate("TaskListWindow", "成品描述:"))
        self.label_2.setText(_translate("TaskListWindow", "成品料号:"))
        self.label_3.setText(_translate("TaskListWindow", "规格描述:"))
        self.search_btn.setText(_translate("TaskListWindow", "查  询"))
        self.allChoose_Rad.setText(_translate("TaskListWindow", "全选"))
        self.inverse_Rad.setText(_translate("TaskListWindow", "反选"))
        self.add_btn.setText(_translate("TaskListWindow", "+"))
        self.del_btn.setText(_translate("TaskListWindow", "-"))
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
        self.pcbInformation_btn.setText(_translate("TaskListWindow", "未\n"
"下\n"
"P\n"
"C\n"
"B\n"
"订\n"
"单"))
        self.waring_labe.setText(_translate("TaskListWindow", "状态栏:"))
        self.combit_rad.setText(_translate("TaskListWindow", "确认"))
        self.comeback_rad.setText(_translate("TaskListWindow", "退回"))
        self.comback_comb.setItemText(0, _translate("TaskListWindow", "请选择退回人员"))
        self.taskCombit_btn.setText(_translate("TaskListWindow", "提交"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TaskListWindow = QtWidgets.QWidget()
    ui = Ui_TaskListWindow()
    ui.setupUi(TaskListWindow)
    TaskListWindow.show()
    sys.exit(app.exec_())
