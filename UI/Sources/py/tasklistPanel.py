from UI.Sources.ui.taskList_UI import Ui_Form
from PyQt5.Qt import *
class TaskList(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = TaskList()
    window.show()
    sys.exit(app.exec_())