from abc import ABCMeta, abstractmethod

class IObserver(metaclass=ABCMeta):
    @abstractmethod
    def createErrorMessageBox(self, message: dict) -> None:
        pass