from View.MainWindow import MainWindow
from Model.PyplotGraphic import PyplotGraphic

class Controller:
    def __init__(self):
        self._view = MainWindow()
        self._model = PyplotGraphic("PyplotGraphic Window", "Graphic", "axis X", "axis Y")

        self._model.attach(self._view)

        self._view.set_signal_add(self._add)
        self._view.set_signal_remove(self._remove)
        self._view.set_signal_show_graphic(self._show)
        self._view.set_signal_clear(self._clear)


    def _add(self) -> None:
        new_item = self._view.ui.lineEdit.text()
        new_item = new_item.replace(" ", "").lower()
        if new_item != "":
            self._view.ui.listBox.addItem(new_item)
            self._view.ui.lineEdit.clear()
            self._model.add(new_item)


    def _remove(self) -> None:
        selected = self._view.ui.listBox.selectedItems()
        for item in selected:
            row = self._view.ui.listBox.row(item)
            self._view.ui.listBox.takeItem(row)
            self._model.remove(row)

    def _clear(self) -> None:
        self._view.ui.listBox.clear()
        self._model.clear()

    def _show(self) -> None:
        self._model.draw()