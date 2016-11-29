# -*- coding: utf-8 -*-
_autor_= "I.C.C."

import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta

class ControladorDron(object):
    __metaclass__ = ABCMeta

    # encender equivale a decir armar motores en OP
    @abc.abstractmethod
    def encender(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def apagar(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getStatus(self):
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getAnguloCabeza(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getCoordenadas(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def irAdelante(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def mantenerCoordenadas(self):
        raise NotImplementedError( "Should have implemented this" )

    # obtiene un diccionario con los modos de operacion que maneja el driver
    # para dron open pilot: estabilizado, acrobático, etc
    @abc.abstractmethod
    def getModosDeOperacion(self):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def setModo(self, modo):
        raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getModo(self):
        raise NotImplementedError( "Should have implemented this" )