from abc import ABCMeta, abstractmethod
from View.IObserver import IObserver

class IObservable(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify(self, message: dict) -> None:
        pass