# -*- coding: utf-8 -*-
from DroneFramework.capaDronAltoNivel.dronVolador import DronVolador
from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero

from scipy.spatial import distance

class DronMulticoptero (DronVolador):

    def __init__(self,controladorMulticoptero):
        """
         :type controladorMulticoptero: ControladorDronMulticoptero
        """
        # inicializa controladorDron, puntoPartida, posicionActual, modo, encendido
        DronVolador.__init__(self,controladorMulticoptero)
        self.controladorMulticoptero=controladorMulticoptero
#Sábado 8 oct.
 #indira
    # Aterriza donde está
    def aterrizar(self):
        self.controladorMulticoptero.aterrizar()

    def aterrizar2(self):
        self.controladorMulticoptero.aterrizar2()

    def bajar(self, distancia, velocidad):
        self.controladorMulticoptero.down(distancia,velocidad)

    def irIzquierda(self, velocidad):
        self.controladorMulticoptero.irIzquierdad(velocidad)

    def irDerecha(self, velocidad):
         self.controladorMulticoptero.irDerecha((velocidad))

 #jorge
    def encender(self):
       self.controladorMulticoptero.encender()

    def subir(self, distancia, velocidad):
        self.controladorMulticoptero.up( distancia,velocidad )

    def irAdelante(self, velocidad):
        self.controladorMulticoptero.irAdelante( velocidad )

    def irAtras(self, velocidad ):
        self.controladorMulticoptero.irAdelante( velocidad )

    def mantener_posicion(self):
        self.controladorMulticoptero.mantenerCoordenadas()

# sábado 22 oct
    def irA(self,x,y,z, velocidad ):
        raise NotImplementedError( "Should have implemented this" )

    def orbitar(self, centro, radio):
        raise NotImplementedError( "Should have implemented this" )

    # dirige la cabeza al punto XYZ
    def mirarA(self,punto3D, velocidad ):
        raise NotImplementedError( "Should have implemented this" )

# sábado 29 oct
    def sobrevolar(self, listaPuntos3D):
        print("hi")
    

# sábado 5 nov




