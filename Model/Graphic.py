from functools import singledispatchmethod

class Graphic:
    def __init__(self, window_title, graphic_title, xlabel, ylabel):
        self._window_title = window_title
        self._graphic_title = graphic_title
        self._xlabel = xlabel
        self._ylabel = ylabel
        self._funcs = []

    def add(self, func):
        self._funcs.append(func)

    def clear(self):
        self._funcs = []

    def get_funcs(self):
        return self._funcs

    @singledispatchmethod
    def remove(self, arg):
        raise NotImplementedError(f"Cannot format value of type {type(arg)}")
    
    @remove.register
    def _(self, arg: int):
        self._funcs.pop(arg)

    @remove.register
    def _(self, arg: str):
        self._funcs.remove(arg)

