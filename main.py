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
        self.ui.pushButton_2.clicked.connect(lambda: self.handlePreview())
        self.ui.searchButton.clicked.connect(lambda: self.search_in_database())

    def connect_database(self):
        self.connection = sqlite3.connect('database/tc.db')
        self.cursor = self.connection.cursor()

    def print_button_ck(self):
        self.set_data()
        self.printDialog()

    def handlePreview(self):
        self.set_data()
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.print_data.print_)
        dialog.exec_()

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        printer.setFullPage(True)
        printer.setPageMargins(0, 0, 0, 0, QPrinter.Millimeter)
        dialog = QPrintDialog(printer, self)
        if dialog.exec_() == QPrintDialog.Accepted:
            self.print_data.print_(printer)

    def set_data(self):
        data = """<html>
    <head>
        <meta content="text/html; charset=UTF-8" http-equiv="content-type">
        <style type="text/css">
            ol {
                margin: 0;
                padding: 0
            }

            table td,table th {
                padding: 0
            }

            .c5 {
                color: #000000;
                font-weight: 400;
                text-decoration: none;
                vertical-align: baseline;
                font-size: 11pt;
                font-family: "Arial";
                font-style: normal
            }

            .c9 {
                color: #000000;
                font-weight: 400;
                text-decoration: none;
                vertical-align: baseline;
                font-family: "Arial";
                font-style: normal
            }

            .c6 {
                padding-top: 0pt;
                padding-bottom: 0pt;
                line-height: 1.2;
                orphans: 2;
                widows: 2;
                text-align: justify
            }

            .c8 {
                padding-top: 0pt;
                padding-bottom: 0pt;
                line-height: 1.2;
                orphans: 2;
                widows: 2;
                text-align: center
            }

            .c10 {
                color: #000000;
                text-decoration: none;
                vertical-align: baseline;
                font-size: 11pt;
                font-style: normal
            }

            .c15 {
                color: #000000;
                text-decoration: none;
                vertical-align: baseline;
                font-style: normal
            }

            .c11 {
                background-color: #ffffff;
                max-width: 538.7pt;
                padding: 7.1pt 28.3pt 28.3pt 28.3pt
            }

            .c1 {
                font-weight: 700;
                font-family: "Nirmala UI"
            }

            .c0 {
                font-weight: 400;
                font-family: "Nirmala UI"
            }

            .c4 {
                font-size: 12pt
            }

            .c7 {
                height: 11pt
            }

            .c14 {
                margin-left: 72pt
            }

            .c3 {
                font-size: 16pt
            }

            .c2 {
                font-weight: 700
            }

            .c12 {
                font-family: "Arial"
            }

            .c13 {
                margin-left: 360pt
            }

            .title {
                padding-top: 24pt;
                color: #000000;
                font-weight: 700;
                font-size: 36pt;
                padding-bottom: 6pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            .subtitle {
                padding-top: 18pt;
                color: #666666;
                font-size: 24pt;
                padding-bottom: 4pt;
                font-family: "Georgia";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                font-style: italic;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            li {
                color: #000000;
                font-size: 11pt;
                font-family: "Arial"
            }

            p {
                margin: 0;
                color: #000000;
                font-size: 11pt;
                font-family: "Arial"
            }

            h1 {
                padding-top: 24pt;
                color: #000000;
                font-weight: 700;
                font-size: 24pt;
                padding-bottom: 6pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            h2 {
                padding-top: 18pt;
                color: #000000;
                font-weight: 700;
                font-size: 18pt;
                padding-bottom: 4pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            h3 {
                padding-top: 14pt;
                color: #000000;
                font-weight: 700;
                font-size: 14pt;
                padding-bottom: 4pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            h4 {
                padding-top: 12pt;
                color: #000000;
                font-weight: 700;
                font-size: 12pt;
                padding-bottom: 2pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            h5 {
                padding-top: 11pt;
                color: #000000;
                font-weight: 700;
                font-size: 11pt;
                padding-bottom: 2pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }

            h6 {
                padding-top: 10pt;
                color: #000000;
                font-weight: 700;
                font-size: 10pt;
                padding-bottom: 2pt;
                font-family: "Arial";
                line-height: 1.1500000000000001;
                page-break-after: avoid;
                orphans: 2;
                widows: 2;
                text-align: left
            }
        </style>
    </head>
    <body class="c11">
        <p class="c8">
            <span class="c0">&#2332;&#2367;&#2354;&#2381;&#2361;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2346;&#2352;&#2367;&#2359;&#2342;</span>
            <span>, </span>
            <span class="c0">&#2351;&#2357;&#2340;&#2350;&#2366;&#2355;</span>
        </p>
        <p class="c8">
            <span class="c1">&#2332;&#2367;</span>
            <span class="c2">. </span>
            <span class="c1">&#2346;</span>
            <span class="c2">. </span>
            <span class="c1">&#2346;&#2381;&#2352;&#2366;&#2341;&#2350;&#2367;&#2325;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2350;&#2352;&#2366;&#2336;&#2368;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2358;&#2366;&#2355;&#2366;</span>
            <span class="c2">, </span>
            <span class="c1">&#2346;&#2367;&#2306;&#2346;&#2352;&#2368;</span>
            <span class="c2">&nbsp;(</span>
            <span class="c1">&#2312;&#2332;&#2366;&#2352;&#2366;</span>
            <span class="c10 c2 c12">)</span>
        </p>
        <p class="c8">
            <span class="c0 c4">&#2350;&#2369;</span>
            <span class="c4">. </span>
            <span class="c0 c4">&#2346;&#2367;&#2306;&#2346;&#2352;&#2368;</span>
            <span class="c4">&nbsp;(</span>
            <span class="c0 c4">&#2312;&#2332;&#2366;&#2352;&#2366;</span>
            <span class="c4">) </span>
            <span class="c0 c4">&#2346;&#2379;</span>
            <span class="c4">. </span>
            <span class="c0 c4">&#2348;&#2366;&#2339;&#2327;&#2366;&#2306;&#2357;</span>
            <span class="c4">&nbsp;</span>
            <span class="c0 c4">&#2340;&#2366;</span>
            <span class="c4">. </span>
            <span class="c0 c4">&#2344;&#2375;&#2352;</span>
            <span class="c4">&nbsp;</span>
            <span class="c0 c4">&#2332;&#2367;</span>
            <span class="c4">. </span>
            <span class="c0 c4">&#2351;&#2357;&#2340;&#2350;&#2366;&#2355;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2350;&#2379;&#2348;&#2366;</span>
            <span>.</span>
            <span class="c0">&#2344;&#2306;</span>
            <span>. : &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2312;</span>
            <span>.</span>
            <span class="c0">&#2350;&#2375;&#2354;</span>
            <span class="c5">&nbsp;: zpschoolpimpri@gmail.com </span>
        </p>
        <p class="c6">
            <span class="c0">&#2309;&#2344;&#2369;&#2325;&#2381;&#2352;&#2350;&#2366;&#2306;&#2325;</span>
            <span>&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2332;&#2344;&#2352;&#2354;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2352;&#2332;&#2367;</span>
            <span>. </span>
            <span class="c0">&#2325;&#2381;&#2352;</span>
            <span class="c5">. </span>
            <span>
        </p>
        <p class="c6">
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2350;&#2366;&#2344;&#2381;&#2351;&#2340;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2381;&#2352;&#2350;&#2366;&#2306;&#2325;</span>
            <span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2350;&#2366;&#2343;&#2381;&#2351;&#2350;</span>
            <span>&nbsp;: </span>
            <span class="c0">&#2350;&#2352;&#2366;&#2336;&#2368;</span>
            <span class="c5">&nbsp;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2351;&#2369;</span>
            <span>.</span>
            <span class="c0">&#2337;&#2366;&#2351;&#2360;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2381;&#2352;</span>
            <span>. : 27140902501 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2348;&#2379;&#2352;&#2381;&#2337;</span>
            <span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2360;&#2306;&#2354;&#2327;&#2381;&#2344;&#2340;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2381;&#2352;&#2350;&#2366;&#2306;&#2325; </span>
            <span class="c5">: </span>
        </p>
        <p class="c8" id="h.gjdgxs">
            <span class="c1 c3">&#2358;&#2366;&#2355;&#2366;</span>
            <span class="c2 c3">&nbsp;</span>
            <span class="c1 c3">&#2360;&#2379;&#2337;&#2354;&#2381;&#2351;&#2366;&#2330;&#2375;</span>
            <span class="c3 c2">&nbsp;</span>
            <span class="c1 c3">&#2346;&#2381;&#2352;&#2350;&#2366;&#2339;&#2346;&#2340;&#2381;&#2352;</span>
        </p>
        <p class="c6">
            <span>&nbsp;</span>
            <span class="c0">&#2357;&#2367;&#2342;&#2381;&#2351;&#2366;&#2352;&#2381;&#2341;&#2368;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2310;&#2351;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2337;&#2368;</span>
            <span class="c5">&nbsp;:""" + self.convertText(self.ui.studentId.text()) + """</span>
        </p>
        <p class="c6">
            <span class="c0">&#2310;&#2343;&#2366;&#2352;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2366;&#2352;&#2381;&#2337;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2381;&#2352;&#2350;&#2366;&#2306;&#2325;</span>
            <span>&nbsp;:</span>
            <span class="c0">&nbsp;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;</span>
            <span>) </span>
            <span class="c0">&#2357;&#2367;&#2342;&#2381;&#2351;&#2366;&#2352;&#2381;&#2341;&#2366;&#2330;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2360;&#2306;&#2346;&#2370;&#2352;&#2381;&#2339;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2344;&#2366;&#2306;&#2357;</span>
            <span>&nbsp;: (</span>
            <span class="c0">&#2344;&#2366;&#2306;&#2357;</span>
            <span>)""" + self.convertText(
            self.ui.name.text() + ' ' + self.ui.fatherName.text() + ' ' + self.ui.lastname.text()) + """&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2357;&#2337;&#2368;&#2354;&#2366;&#2306;&#2330;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2344;&#2366;&#2306;&#2357;</span>
            <span class="c5">&nbsp;"""+ self.convertText(self.ui.fatherName.text()) + """</span>
        </p>
        <p class="c6">
            <span>&nbsp;&nbsp;(</span>
            <span class="c0">&#2310;&#2337;&#2344;&#2366;&#2306;&#2357;</span>
            <span>)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2408;</span>
            <span>) </span>
            <span class="c0">&#2310;&#2312;&#2330;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2344;&#2366;&#2306;&#2357;</span>
            <span class="c5">&nbsp;:""" + self.convertText(self.ui.mothername.text()) + """</span>
        </p>
        <p class="c6">
            <span class="c0">&#2409;</span>
            <span>) </span>
            <span class="c0">&#2352;&#2366;&#2359;&#2381;&#2335;&#2381;&#2352;&#2368;&#2351;&#2340;&#2381;&#2357;</span>
            <span>&nbsp;- </span>
            <span class="c0">&#2349;&#2366;&#2352;&#2340;&#2368;&#2351;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2410;</span>
            <span>) </span>
            <span class="c0">&#2350;&#2366;&#2340;&#2371;&#2349;&#2366;&#2359;&#2366;</span>
            <span>&nbsp;: </span>
            <span class="c1">&#2350;&#2352;&#2366;&#2336;&#2368;</span>
            <span class="c2">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2411;</span>
            <span>) </span>
            <span class="c0">&#2343;&#2352;&#2381;&#2350;</span>
            <span>&nbsp;: - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2412;</span>
            <span>) </span>
            <span class="c0">&#2332;&#2366;&#2340;</span>
            <span>&nbsp;: -&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2413;</span>
            <span>) </span>
            <span class="c0">&#2346;&#2379;&#2335;&#2332;&#2366;&#2340;</span>
            <span class="c5">:</span>
        </p>
        <p class="c6">
            <span class="c0">&#2414;</span>
            <span>) </span>
            <span class="c0">&#2332;&#2344;&#2381;&#2350;&#2360;&#2381;&#2341;&#2355;</span>
            <span>&nbsp;(</span>
            <span class="c0">&#2327;&#2366;&#2306;&#2357;</span>
            <span>/</span>
            <span class="c0">&#2358;&#2361;&#2352;</span>
            <span>) :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2340;&#2366;&#2354;&#2369;&#2325;&#2366;</span>
            <span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2332;&#2367;&#2354;&#2381;&#2361;&#2366;</span>
            <span class="c5">: </span>
        </p>
        <p class="c6">
            <span class="c0">&nbsp;&nbsp;&nbsp;&#2352;&#2366;&#2332;&#2381;&#2351;</span>
            <span>&nbsp;: </span>
            <span class="c1">&#2350;&#2361;&#2366;&#2352;&#2366;&#2359;&#2381;&#2335;&#2381;&#2352;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2342;&#2375;&#2358;</span>
            <span>&nbsp;: </span>
            <span class="c1">&#2349;&#2366;&#2352;&#2340;</span>
            <span class="c2">&nbsp;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2415;</span>
            <span>) </span>
            <span class="c0">&#2311;</span>
            <span>. </span>
            <span class="c0">&#2360;&#2344;&#2366;&#2346;&#2381;&#2352;&#2350;&#2366;&#2339;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2332;&#2344;&#2381;&#2350;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2342;&#2367;&#2344;&#2366;&#2306;&#2325;</span>
            <span class="c5">&nbsp;:</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2406;</span>
            <span>) </span>
            <span class="c0">&#2332;&#2344;&#2381;&#2350;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2342;&#2367;&#2344;&#2366;&#2306;&#2325;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2309;&#2325;&#2381;&#2359;&#2352;&#2368;</span>
            <span class="c5">: </span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2407;</span>
            <span>) </span>
            <span class="c0">&#2351;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2346;&#2370;&#2352;&#2381;&#2357;&#2368;&#2330;&#2368;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2357;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2311;&#2351;&#2340;&#2381;&#2340;&#2366;</span>
            <span class="c5">&nbsp;:</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2408;</span>
            <span>) </span>
            <span class="c0">&#2351;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2358;&#2366;&#2355;&#2375;&#2340;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2346;&#2381;&#2352;&#2357;&#2375;&#2358;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2328;&#2375;&#2340;&#2354;&#2381;&#2351;&#2366;&#2330;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2342;&#2367;&#2344;&#2366;&#2306;&#2325;</span>
            <span>:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2311;&#2351;&#2340;&#2381;&#2340;&#2366;</span>
            <span class="c5">: </span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2409;</span>
            <span>) </span>
            <span class="c0">&#2309;&#2349;&#2381;&#2351;&#2366;&#2360;&#2366;&#2340;&#2368;&#2354;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2346;&#2381;&#2352;&#2327;&#2340;&#2368;</span>
            <span>&nbsp;: </span>
            <span class="c0">&#2360;&#2366;&#2343;&#2366;&#2352;&#2339;</span>
            <span>/</span>
            <span class="c0">&#2330;&#2366;&#2306;&#2327;&#2354;&#2368;</span>
            <span>/</span>
            <span class="c0">&#2360;&#2350;&#2366;&#2343;&#2366;&#2344;&#2325;&#2366;&#2352;&#2325;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2357;&#2352;&#2381;&#2340;&#2339;&#2370;&#2325;</span>
            <span>&nbsp;: </span>
            <span class="c0">&#2330;&#2366;&#2306;&#2327;&#2354;&#2368;</span>
            <span>/</span>
            <span class="c0">&#2360;&#2350;&#2366;&#2343;&#2366;&#2344;&#2325;&#2366;&#2352;&#2325;</span>
            <span class="c5">&nbsp;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2410;</span>
            <span>) </span>
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2360;&#2379;&#2337;&#2354;&#2381;&#2351;&#2366;&#2330;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2342;&#2367;&#2344;&#2366;&#2306;&#2325;</span>
            <span class="c5">&nbsp;:</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2411;</span>
            <span>) </span>
            <span class="c0">&#2325;&#2379;&#2339;&#2340;&#2381;&#2351;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2311;&#2351;&#2340;&#2381;&#2340;&#2375;&#2340;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2358;&#2367;&#2325;&#2340;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2361;&#2379;&#2340;&#2366;</span>
            <span class="c5">&nbsp;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2412;</span>
            <span>) </span>
            <span class="c0">&#2325;&#2375;&#2357;&#2381;&#2361;&#2366;&#2346;&#2366;&#2360;&#2369;&#2344;</span>
            <span>&nbsp;(</span>
            <span class="c0">&#2309;&#2306;&#2325;&#2368;</span>
            <span class="c5">) : - </span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2413;</span>
            <span>) </span>
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2360;&#2379;&#2337;&#2339;&#2381;&#2351;&#2366;&#2330;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2366;&#2352;&#2339;</span>
            <span class="c5">&nbsp;: </span>
        </p>
        <p class="c6">
            <span class="c0">&#2407;&#2414;</span>
            <span>) </span>
            <span class="c0">&#2358;&#2375;&#2352;&#2366;</span>
            <span class="c5">:</span>
        </p>
        <p class="c6">
            <span class="c5">&nbsp;</span>
        </p>
        <p class="c6 c14">
            <span class="c1">&#2342;&#2366;&#2326;&#2354;&#2366;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2342;&#2375;&#2339;&#2381;&#2351;&#2366;&#2340;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2351;&#2375;&#2340;&#2379;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2325;&#2368;</span>
            <span class="c2">, </span>
            <span class="c1">&#2357;&#2352;&#2368;&#2354;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2350;&#2366;&#2361;&#2367;&#2340;&#2368;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2358;&#2366;&#2355;&#2375;&#2340;&#2368;&#2354;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2332;&#2344;&#2352;&#2354;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2352;&#2332;&#2367;&#2360;&#2381;&#2335;&#2352;</span>
            <span class="c2">&nbsp;</span>
            <span class="c1">&#2325;&#2381;&#2352;</span>
            <span class="c2">. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c1">&#2346;&#2381;&#2352;&#2350;&#2366;&#2339;&#2375;</span>
        </p>
        <p class="c6">
            <span class="c0">&#2340;&#2366;&#2352;&#2368;&#2326;</span>
            <span class="c5">:</span>
        </p>
        <p class="c6 c7">
            <span class="c5"></span>
        </p>
        <p class="c6 c7">
            <span class="c5"></span>
        </p>
        <p class="c6">
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2350;&#2369;&#2326;&#2381;&#2351;&#2366;&#2343;&#2381;&#2351;&#2366;&#2346;&#2325;</span>
        </p>
        <p class="c6">
            <span class="c0">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&#2357;&#2352;&#2381;&#2327;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2358;&#2367;&#2325;&#2381;&#2359;&#2325;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2354;&#2375;&#2326;&#2344;&#2367;&#2325;</span>
            <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>
            <span class="c0">&#2332;&#2367;</span>
            <span>.</span>
            <span class="c0">&#2346;</span>
            <span>.</span>
            <span class="c0">&#2346;&#2381;&#2352;&#2366;</span>
            <span>.</span>
            <span class="c0">&#2350;</span>
            <span>.</span>
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2346;&#2367;&#2306;&#2346;&#2352;&#2368;</span>
            <span>&nbsp;(</span>
            <span class="c0">&#2312;&#2332;&#2366;&#2352;&#2366;</span>
            <span class="c5">)</span>
        </p>
        <p class="c6 c13">
            <span class="c0">&nbsp;&nbsp;&nbsp;&#2346;&#2306;</span>
            <span>.</span>
            <span class="c0">&#2360;</span>
            <span>. </span>
            <span class="c0">&#2344;&#2375;&#2352;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2332;&#2367;</span>
            <span>.</span>
            <span class="c0">&#2346;</span>
            <span>. </span>
            <span class="c0 c10">&#2351;&#2357;&#2340;&#2350;&#2366;&#2355;</span>
        </p>
        <p class="c6 c7">
            <span class="c10 c0"></span>
        </p>
        <p class="c6">
            <span class="c0">&#2335;&#2367;&#2346;</span>
            <span>&nbsp;:- </span>
            <span class="c0">&#2407;</span>
            <span>) </span>
            <span class="c0">&#2358;&#2366;&#2355;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2360;&#2379;&#2337;&#2354;&#2381;&#2351;&#2366;&#2330;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2342;&#2366;&#2326;&#2354;&#2381;&#2351;&#2366;&#2350;&#2343;&#2381;&#2351;&#2375;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2309;&#2344;&#2366;&#2343;&#2367;&#2325;&#2371;&#2340;&#2352;&#2367;&#2340;&#2381;&#2351;&#2366;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2348;&#2342;&#2354;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2375;&#2354;&#2381;&#2351;&#2366;&#2360;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2360;&#2306;&#2348;&#2306;&#2343;&#2367;&#2340;&#2366;&#2306;&#2357;&#2352;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2366;&#2351;&#2342;&#2375;&#2358;&#2368;&#2352;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2366;&#2352;&#2357;&#2366;&#2312;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2325;&#2352;&#2339;&#2381;&#2351;&#2366;&#2340;</span>
            <span>&nbsp;</span>
            <span class="c0">&#2351;&#2375;&#2312;&#2354;</span>
            <span class="c5">.</span>
        </p>
    </body>
</html>
"""
        self.print_data.setHtml(data)

    def convertText(self, QString):
        outputString = ''
        conv = {'a': '\u0902', '%': '\u0903', 'v': '\u0905', 'b': '\u0907', 'm': '\u0909', '_': '\u090b', ',': '\u090f',
                'd': '\u0915',
                'x': '\u0917', 'p': '\u091a', 'N': '\u091b', 't': '\u091c', '>': '\u091d', '=': '\u091e', 'V': '\u091f',
                'B': '\u0920', 'M': '\u0921', '<': '\u0922', 'r': '\u0924', 'n': '\u0926', 'u': '\u0928', 'i': '\u092a',
                'Q': '\u092b', 'c': '\u092c', 'e': '\u092e', ';': '\u092f', 'j': '\u0930', 'y': '\u0932', 'G': '\u0933',
                'o': '\u0935', 'l': '\u0938', 'g': '\u0939', '*': '\u093a', 'k': '\u093e', 'f': '\u093f', 'h': '\u0940',
                'D': '\u0941',
                'w': '\u0942', '`': '\u0943', 'W': '\u0945', 's': '\u0947', 'S': '\u0948', '~': '\u094d', '^': '\u0951',
                'A': '\u0964',
                '0': '\u0966', '1': '\u0967', '2': '\u0968', '3': '\u0969', '4': '\u096a', '5': '\u096b', '6': '\u096c',
                '7': '\u096d', '8': '\u096e', '9': '\u096f', 'z': '&#2381;&#2352;', 'J': '&#2358;&#2381;&#2352;',
                'K': '&#2332;&#2381;&#2334;', '+': '&#2340;&#2381;&#2352;',
                '#': '&#2352;&#2369;', ':': '&#2352;&#2370;', '\u005c': '\u097d', '-': '.', ' ': '&nbsp;'}

        for i in QString:
            outputString = outputString + conv[i]
        return outputString

    def search_in_database(self):
        id = self.ui.studentId.text()
        self.cursor.execute('SELECT * FROM student WHERE studenId = ?', id)
        data = self.cursor.fetchall()
        self.populate(data)

    def populate(self, values):
        self.ui.name.setText(values[2])
        self.ui.middleName.setText(values[3])
        self.ui.lastname.setText(values[3])
        self.ui.fatherName.setText(values[4])
        self.ui.mothername.setText(values[5])
        self.ui.religion.setText(values[6])
        self.ui.caste.setText(values[7])
        self.ui.subcaste.setText(values[8])
        self.ui.dob.setText(values[9])
        self.ui.bobInCal.setDate(values[10])
        self.ui.formerSchool.setText(values[11])
        self.ui.addDate.setDate(values[12])
        self.ui.schoolLeft.setDate(values[11])
        self.ui.formerClass.setText(values[12])
        self.ui.class_2.setText(values[13])
        self.ui.leavingReason.setPlainText(values[14])

    def __del__(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    preRunChecks = startup.Checks()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
