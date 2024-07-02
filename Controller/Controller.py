from View.MainWindow import MainWindow
from Model.PyplotGraphic import PyplotGraphic

class Controller:
    def __init__(self):
        self._view = MainWindow()
        self._model = PyplotGraphic("PyplotGraphic Window", "Graphic", "axis X", "axis Y")

        self._view.set_signal_add(self.add)
        self._view.set_signal_remove(self.remove)
        self._view.set_signal_show_graphic(self.show)


    def add(self):
        new_item = self._view.ui.lineEdit.text()
        new_item = new_item.replace(" ", "")
        if new_item != "":
            self._view.ui.listBox.addItem(new_item)
            self._view.ui.lineEdit.clear()
            self._model.add(new_item)


    def remove(self):
        selected = self._view.ui.listBox.selectedItems()
        for item in selected:
            row = self._view.ui.listBox.row(item)
            self._view.ui.listBox.takeItem(row)
            self._model.remove(row)


    def show(self):
        self._model.draw()