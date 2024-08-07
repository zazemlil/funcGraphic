from abc import ABCMeta, abstractmethod

class IWindow(metaclass=ABCMeta):
    @abstractmethod
    def set_signal_show_graphic(self, arg) -> None:
        pass

    @abstractmethod
    def set_signal_add(self, arg) -> None:
        pass

    @abstractmethod
    def set_signal_remove(self, arg) -> None:
        pass

    @abstractmethod
    def set_signal_clear(self, arg) -> None:
        pass

    @abstractmethod
    def set_signal_text_changed(self, arg) -> None:
        pass

    @abstractmethod
    def set_signal_input_text_editing_finished(self, arg) -> None:
        pass