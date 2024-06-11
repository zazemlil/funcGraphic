from abc import ABCMeta, abstractmethod

class IWindow(metaclass=ABCMeta):
    @abstractmethod
    def set_signal_show_graphic(self):
        pass