from abc import abstractmethod
from abc import ABCMeta


class Mando(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def alta():
        pass

    @staticmethod
    @abstractmethod
    def baja():
        pass

    @staticmethod
    @abstractmethod
    def modificar():
        pass

    @staticmethod
    @abstractmethod
    def buscar():
        pass

    @staticmethod
    @abstractmethod
    def mostrarTodos():
        pass