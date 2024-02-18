from abc import abstractmethod
from abc import ABCMeta


class iGestores(metaclass=ABCMeta):
    '''
    Clase interfaz encargada de permitir que se puedan llamar a los "mismas" funciones desde el menu
    '''
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
    def menuModificar():
        pass

    @staticmethod
    @abstractmethod
    def buscar():
        pass

    @staticmethod
    @abstractmethod
    def mostrarTodos():
        pass
