from abc import ABCMeta, abstractmethod

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def add(self, func: str) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def remove(self, arg: int | str) -> None:
        pass

    @abstractmethod
    def change(self, new_func: str, index: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass