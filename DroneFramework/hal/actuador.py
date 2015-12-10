import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta

class Actuador (object):
    __metaclass__ = ABCMeta

    def __init__(self):
        # este sera un diccionario
        self.actuadorData = None
        self.status = None
        self.driver = None

    @abc.abstractmethod
    def setData(self):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )


    @abc.abstractmethod
    def getStatus(self):
        #devuelve el estado del actuador
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def encender(self):
        #inicializa y pone en ON el actuador
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def apagar(self):
        # apaga el actuador
         raise NotImplementedError( "Should have implemented this" )