from abc import ABCMeta, abstractmethod

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def add(self, func) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def remove(self, arg) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass