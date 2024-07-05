from typing import override
from PyQt6.uic import load_ui as lu
from View.IWindow import IWindow

class MainWindow(IWindow):
    def __init__(self):
        self.ui = lu.loadUi("Utilz/Windows/MainWindow.ui")
        self.ui.setFixedSize(self.ui.frameSize().width(), self.ui.frameSize().height())
        self.ui.show()

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
