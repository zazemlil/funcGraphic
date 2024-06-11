from typing import override
from PyQt6.uic import load_ui as lu
from View.IWindow import IWindow

class MainWindow(IWindow):
    def __init__(self):
        self.ui = lu.loadUi("Utilz/Windows/MainWindow.ui")
        self.ui.show()

    @override
    def set_signal_show_graphic(self):
        pass
