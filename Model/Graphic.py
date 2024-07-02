from typing import override
from functools import singledispatchmethod
from Model.IGraphic import IGraphic

class Graphic(IGraphic):
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        self._window_title = window_title
        self._graphic_title = graphic_title
        self._xlabel = xlabel
        self._ylabel = ylabel
        self._funcs = []

    @override
    def add(self, func):
        func = func.replace(" ", "")
        self._funcs.append(func)

    @override
    def clear(self):
        self._funcs = []

    def get_funcs(self):
        return self._funcs

    @override
    @singledispatchmethod
    def remove(self, arg):
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")
    
    @remove.register
    def _(self, arg: int):
        self._funcs.pop(arg)

    @remove.register
    def _(self, arg: str):
        self._funcs.remove(arg)

