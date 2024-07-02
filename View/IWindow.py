from abc import ABCMeta, abstractmethod

class IWindow(metaclass=ABCMeta):
    @abstractmethod
    def set_signal_show_graphic(self, arg):
        pass

    @abstractmethod
    def set_signal_add(self, arg):
        pass

    @abstractmethod
    def set_signal_remove(self, arg):
        pass