# -*- coding: utf-8 -*-
_autor_= "I.C.C."

import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from controladorDron import ControladorDron

class ControladorDronVolador(ControladorDron):
    __metaclass__ = ABCMeta

   # giro lateral de la cabeza
    @abc.abstractmethod
    def yaw(self, grados, velocidad):
        # pone los datos que viene en forma de diccionario de la capa controlador Dron
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de la cabeza a la izquierda
    @abc.abstractmethod
    def yaw_izquierda(self, grados, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de la cabeza a la derecha
    @abc.abstractmethod
    def yaw_derecha(self, grados, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # elevar el dron
    @abc.abstractmethod
    def up(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # bajar el dron
    @abc.abstractmethod
    def down(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # cabeceo - elevación de la cabeza
    @abc.abstractmethod
    def pitch_arriba(self, grados, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # cabeceo - bajar la cabeza
    @abc.abstractmethod
    def pitch_abajo(self, grados, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de costado a la derecha
    @abc.abstractmethod
    def roll_derecha(self, grados, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # giro lateral de costado a la izquierda
    @abc.abstractmethod
    def roll_izquierda(self, grados,velocidad):
        raise NotImplementedError( "Should have implemented this" )

    # me da la distancia del dron al suelo
    @abc.abstractmethod
    def getDistanciaSuelo(self):
        raise NotImplementedError( "Should have implemented this" )

    # dirige el dron hacia la dirección que apunta la cabeza
    @abc.abstractmethod
    def irAdelante(self):
        raise NotImplementedError( "Should have implemented this" )

    # obtiene los ángulos x, y,  z del giroscopio, que son los angulos de inclinación de la cabeza
    @abc.abstractmethod
    def getAnguloCabeza(self):
        raise NotImplementedError( "Should have implemented this" )


