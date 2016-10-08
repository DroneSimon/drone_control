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

#hacer función extra para probar funciones


 #jorge
    def encender(self):
       self.controladorMulticoptero.encender()

    def subir(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )
    def irAdelante(self, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def irAtras(self, velocidad ):
        raise NotImplementedError( "Should have implemented this" )

    def mantener_posicion(self):
        raise NotImplementedError( "Should have implemented this" )

# sábado 15 oct
#jorge

    def irIzquierda(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def irDerecha(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def orbitar(self, centro, radio):
        raise NotImplementedError( "Should have implemented this" )


#Indira
    def irAdelante(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def irAtras(self,distancia, velocidad ):
        raise NotImplementedError( "Should have implemented this" )

    def irA(self,x,y,z, velocidad ):
        raise NotImplementedError( "Should have implemented this" )

    # dirige la cabeza al punto XYZ
    def mirarA(self,punto3D, velocidad ):
        raise NotImplementedError( "Should have implemented this" )


# sábado 22 oct

# sábado 29 oct
    def sobrevolar(self, listaPuntos3D):
        print("hi")
    

# sábado 5 nov




