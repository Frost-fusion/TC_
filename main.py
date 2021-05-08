import sqlite3
import sys

from PyQt5 import QtGui
from PyQt5.QtPrintSupport import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit

import startup
from main_ui import Ui_Form


class MainWindow(QMainWindow):
    cursor: sqlite3.Cursor

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connection = None
        self.connect_database()
        font = QtGui.QFont()
        font.setFamily("Kruti Dev 010")
        QApplication.setFont(font)
        self.print_data = QTextEdit("")
        self.ui.please.clicked.connect(lambda: self.print_button_ck())

    def connect_database(self):
        self.connection = sqlite3.connect('database/tc.db')
        self.cursor = self.connection.cursor()

    def print_button_ck(self):
        self.set_data()
        self.printDialog()

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.print_data.print_(printer)

    def set_data(self):
        data = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                    <html>
                        <head>
                            <meta name="qrichtext" content="1"/>
                            <style type="text/css">
                                p, li {
                                   white-space: pre-wrap;
                               }
                            </style>
                        </head>
                        <body style=" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;">
                            <p style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
                                <br/>
                            </p>
                            """+ self.convertText(self.ui.classLineEdit.text())+ """
                        </body>
                    </html>
                """
        self.print_data.setText(data)

    def convertText(self, QString):
        outputString = ''
        conv = {'a': '\u0902', '%': '\u0903', 'v': '\u0905', 'b': '\u0907', 'm': '\u0909', '_': '\u090b', ',': '\u090f', 'd': '\u0915',
                'x': '\u0917', 'p': '\u091a', 'N': '\u091b', 't': '\u091c', '>': '\u091d', '=': '\u091e', 'V': '\u091f',
                'B': '\u0920', 'M': '\u0921', '<': '\u0922', 'r': '\u0924', 'n': '\u0926', 'u': '\u0928', 'i': '\u092a',
                'Q': '\u092b', 'c': '\u092c', 'e': '\u092e', ';': '\u092f', 'j': '\u0930', 'y': '\u0932', 'G': '\u0933',
                'o': '\u0935', 'l': '\u0938', 'g': '\u0939', '*': '\u093a', 'k': '\u093e', 'f': '\u093f', 'h': '\u0940', 'D': '\u0941',
                'w': '\u0942', '`': '\u0943', 'W': '\u0945', 's': '\u0947', 'S': '\u0948', '~': '\u094d', '^': '\u0951', 'A': '\u0964',
                '0': '\u0966', '1': '\u0967', '2': '\u0968', '3': '\u0969', '4': '\u096a', '5': '\u096b', '6': '\u096c',
                '7': '\u096d', '8': '\u096e', '9': '\u096f', 'z': '&#2381;&#2352;', 'J': '&#2358;&#2381;&#2352;', 'K': '&#2332;&#2381;&#2334;', '+': '&#2340;&#2381;&#2352;',
                '#': '&#2352;&#2369;', ':': '&#2352;&#2370;', '\u005c': '\u097d', '-': '.', ' ': '&nbsp;'}

        for i in QString:
            outputString = outputString + conv[i]
        return outputString

    def __del__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    preRunChecks = startup.Checks()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
