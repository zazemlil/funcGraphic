from View.MainWindow import MainWindow
from Model.PyplotGraphic import PyplotGraphic
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QListWidgetItem
from PyQt6.QtGui import *

class Controller:
    def __init__(self):
        self._view = MainWindow()
        self._model = PyplotGraphic("PyplotGraphic Window", "Graphic", "axis X", "axis Y")

        self._model.attach(self._view)

        self._view.set_signal_add(self._add)
        self._view.set_signal_remove(self._remove)
        self._view.set_signal_show_graphic(self._show)
        self._view.set_signal_clear(self._clear)
        self._view.set_signal_text_changed(self._text_changed)
        self._view.set_signal_input_text_editing_finished(self._add)

        self._set_min_max_freq_X()


    def _add(self) -> None:
        new_item_text = self._view.ui.lineEdit.text()
        new_item_text = new_item_text.replace(" ", "").lower()
        if new_item_text != "":
            item = QListWidgetItem(new_item_text)
            item.setFlags(Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)
            self._view.ui.listBox.addItem(item)
            self._view.ui.lineEdit.clear()
            self._model.add(new_item_text)


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
        self._view.ui.listBox.blockSignals(True)
        self._set_default_item_color()
        self._set_min_max_freq_X() # ----------------------------------
        self._model.draw()
        self._view.ui.listBox.blockSignals(False)

    def _text_changed(self, item) -> None:
        self._view.ui.listBox.blockSignals(True)

        item.setText(item.text().replace(" ", ""))
        index = self._view.ui.listBox.indexFromItem(item).row()
        self._model.change(item.text(), index)
        foregroundBrush = QBrush(QColor(255,165,0))
        self._view.ui.listBox.item(index).setForeground(foregroundBrush)

        self._view.ui.listBox.blockSignals(False)

    def _set_default_item_color(self) -> None:
        foregroundBrush = QBrush(QColor(0,0,0))
        for i in range(self._view.ui.listBox.count()):
            self._view.ui.listBox.item(i).setForeground(foregroundBrush)

    def _set_min_max_freq_X(self) -> None:
        minX = self._view.ui.lineEdit_minX.text()
        maxX = self._view.ui.lineEdit_maxX.text()
        step = self._view.ui.lineEdit_step.text()
        
        if minX.isdigit():
            self._model.set_minX(float(minX))
            print("minX = ", self._model._minX)
        else:
            self._model.set_minX(-22)
            self._view.ui.lineEdit_minX.setText("-22")

        if maxX.isdigit():
            self._model.set_maxX(float(maxX))
            print("maxX = ", self._model._maxX)
        else:
            self._model.set_maxX(-22)
            self._view.ui.lineEdit_maxX.setText("22")
        
        if step.isdigit():
            self._model.set_freq(float(step))
            print("step = ", self._model._step)
        else:
            self._model.set_freq(0.5)
            self._view.ui.lineEdit_step.setText("0.5")
