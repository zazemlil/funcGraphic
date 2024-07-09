from typing import override, List
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

    @override
    def attach(self, observer: IObserver) -> None:
        self._observers.append(observer)

    @override
    def detach(self, observer: IObserver) -> None:
        self._observers.remove(observer)

    @override
    def notify(self, message: dict) -> None:
        for observer in self._observers:
            observer.createErrorMessageBox(message)

    @override
    def add(self, func) -> None:
        func = func.replace(" ", "")
        self._funcs.append(func)

    @override
    def clear(self) -> None:
        self._funcs = []

    @override
    @singledispatchmethod
    def remove(self, arg) -> None:
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")
    
    @remove.register
    def _(self, arg: int) -> None:
        self._funcs.pop(arg)

    @remove.register
    def _(self, arg: str) -> None:
        self._funcs.remove(arg)

