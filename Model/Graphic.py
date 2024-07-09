from typing import List
from functools import singledispatchmethod
from Model.IGraphic import IGraphic
from Model.IObservable import IObservable
from View.IObserver import IObserver

class Graphic(IGraphic, IObservable):
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        self._observers: List[IObserver] = []

        self._window_title = window_title
        self._graphic_title = graphic_title
        self._xlabel = xlabel
        self._ylabel = ylabel
        self._funcs = []

    def attach(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def detach(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    def notify(self, message: dict) -> None:
        for observer in self._observers:
            observer.createErrorMessageBox(message)

    def add(self, func: str) -> None:
        func = func.replace(" ", "").lower()
        self._funcs.append(func)

    def clear(self) -> None:
        self._funcs = []

    def change(self, new_func: str, index: int) -> None:
        self._funcs[index] = new_func

    @singledispatchmethod
    def remove(self, arg) -> None:
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")
    
    @remove.register
    def _(self, arg: int) -> None:
        self._funcs.pop(arg)

    @remove.register
    def _(self, arg: str) -> None:
        self._funcs.remove(arg)

