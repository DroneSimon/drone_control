import abc
from abc import ABCMeta


class Driver(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def getData(self):
        # devuelve los datos como un diccionario:
        #       datos: diccionario con los datos
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getStatus(self):
        # tiene los datos del sensor
        # ok, no_ok, excepcion,
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def forceRead(self):
        # fuerza a hacer una nueva lectura al sensor
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def reset(self):
        # inicializa datos sensor
        raise NotImplementedError( "Should have implemented this" )

