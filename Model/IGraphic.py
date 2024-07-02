from abc import ABCMeta, abstractmethod

class IGraphic(metaclass=ABCMeta):
    @abstractmethod
    def add(self, func):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def remove(self, arg):
        pass

    @abstractmethod
    def draw(self):
        pass