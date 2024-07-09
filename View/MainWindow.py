from typing import override
from PyQt6.uic import load_ui as lu
from PyQt6.QtWidgets import QMessageBox
from View.IWindow import IWindow
from View.IObserver import IObserver

class MainWindow(IWindow, IObserver):
    def __init__(self):
        self.ui = lu.loadUi("Utilz/Windows/MainWindow.ui")
        self.ui.setFixedSize(self.ui.frameSize().width(), self.ui.frameSize().height())

        urlLink="<a style=\"text-decoration: none\" href=\"https://numpy.org/doc/stable/reference/routines.math.html\">Справочник</a>"
        self.ui.lb_info.setText(urlLink)
        self.ui.lb_info.setOpenExternalLinks(True)

        self.ui.show()

    @override
    def createErrorMessageBox(self, message: Exception) -> None:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText("Ошибка при построении графика! Посмотрите подробную информацию об ошибке (Show Details...).")
        msg.setDetailedText(str(message))
        msg.setWindowTitle("Error")
        msg.exec()

    @override
    def set_signal_show_graphic(self, arg):
        self.ui.pb_show.clicked.connect(arg)

    @override
    def set_signal_add(self, arg):
        self.ui.pb_add.clicked.connect(arg)

    @override
    def set_signal_remove(self, arg):
        self.ui.pb_remove.clicked.connect(arg)

    @override
    def set_signal_clear(self, arg):
        self.ui.pb_clear.clicked.connect(arg)
