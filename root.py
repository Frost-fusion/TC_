import sys
from PySide6.QtWidgets import QApplication, QMainWindow
import sqlite3
from root_ui import Ui_Form


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


def systemGoodCheck():
    cursor: sqlite3.Cursor


if __name__ == "__main__":
    app = QApplication(sys.argv)
    if systemGoodCheck():
        sys.exit(1)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
# this is constructed as per QT docs for invoking a ui -> py file and load application asa well as gui.

#implementation expected:
#root.py is project start script-> it checks if database is constructed or not tthen do it so
# then call main.py to initiate application and show GUI,which is main.ui converted to main_ui.py
# the complete application will be runed from main.py

# Software structure suggestion will be accepted