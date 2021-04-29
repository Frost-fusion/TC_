from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit
import sys
from PySide6.QtGui import QIcon, QFont, QAction
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog, QPrintDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

    def exit_app(self):
        self.close()

    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)

        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()

    def print_preview(self, printer):
        self.textEdit.print_(printer)

    def print_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)


myapp = QApplication(sys.argv)
window = Window()
myapp.exec_()
sys.exit()
