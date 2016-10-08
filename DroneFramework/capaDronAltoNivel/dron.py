# -*- coding: utf-8 -*-

import abc
# Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
from DroneFramework.capaDronBajoNivel.controladorDron import ControladorDron
from scipy.spatial import distance


class Dron (object):
    __metaclass__ = ABCMeta

    def __init__(self,controladorDron):
        """
        :type controladorDron: ControladorDron
        """
        # Este es un controlador con funciones de nivel intermedio en la comunicación del dron
        self.encendido=False
        self.modo=None
        self.puntoPartida=controladorDron.getCoordenadas()
        self.posicionActual=controladorDron.getCoordenadas()

    def volver(self,velocidad):
        self.irA(self.puntoPartida,velocidad)

    #calcula la distancia euclideana entre dos puntos, donde p1 y p2 son dos diccionarios con (x,y,z)
    def distancia3d(self,p1,p2):
        return distance.euclidean((p1['x'],p1['y'],p1['z']),(p2['x'],p2['y'],p2['z']))

    @abc.abstractmethod
    # dirige la cabeza al punto XYZ, que es un diccionario con x,y,z
    def mirarA(self, puntoXYZ):
        raise NotImplementedError( "Should have implemented this" )

    # En el caso del Open Pilot la velocidad 0-30 aproximadamente
    #  dependerá en cuanto se calibró la velocidad de estable (throtle)
    def irA(self, puntoDestino, velocidad):
        self.mirarA(puntoDestino)
        self.controladorDron.irAdelante(velocidad)
        direccionX=1
        if (self.posicionActual['x']>puntoDestino['x']):
            direccionX=-1

        direccionY=1
        if (self.posicionActual['y']>puntoDestino['y']):
            direccionY=-1

        faltaX=True
        faltaY=True
        while ( faltaX & faltaY):
            self.posicionActual=self.controladorDron.getCoordenadas()
            if (direccionX==1):
                faltaX=self.posicionActual['x']<puntoDestino['x'] # si x destino esta a la derecha
            else:
                faltaX=self.posicionActual['x']>puntoDestino['x'] # si x destino esta a la izquierda

            if (direccionY==1):
                faltaY=self.posicionActual['y']<puntoDestino['y'] # si y destino esta al norte
            else:
                faltaY=self.posicionActual['y']>puntoDestino['y'] # si y destino esta al sud

        self.controladorDron.mantenerCoordenadas()

        direccionZ=1
        if (self.posicionActual['z']>puntoDestino['Z']):
            direccionX=-1

        faltaZ=True
        while ( faltaZ):
            self.posicionActual=self.controladorDron.getCoordenadas()
            if (direccionZ==1):
                faltaX=self.posicionActual['z']<puntoDestino['z'] # si z destino esta a arriba
            else:
                faltaX=self.posicionActual['z']>puntoDestino['z'] # si z destino esta abajo


    def encender(self):
        self.controladorDron.encender()

    def apagar(self):
        self.controladorDron.apagar()

    # devuelve un diccionario con la posición x,y,z del dron donde z es la altura del piso
    def getCoordenadas(self):
        self.posicionActual=self.controladorDron.getCoordenadas()
        return self.posicionActual

    def setPuntoPartida(self):
        self.posicionActual=self.controladorDron.getCoordenadas()
        self.puntoPartida=self.posicionActual
        return self.puntoPartida

    def mantenerCoordenadas(self):
        self.controladorDron.mantenerCoordenadas()

    def irAdelante(self,velocidad):
        self.controladorDron.irAdelante(velocidad)




