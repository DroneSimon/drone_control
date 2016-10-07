from DroneFramework.capaDronAltoNivel.dronVolador import DronVolador
from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero

from scipy.spatial import distance

class DronMulticoptero (DronVolador):

    def __init__(self,controladorMulticoptero):
        """
        :type controladorMulticoptero: ControladorDronMulticoptero
        """
        # inicializa controladorDron, puntoPartida, posicionActual, modo, encendido
        DronVolador.__init__(controladorMulticoptero)
#Sábado 8 oct.
 #indira
    # Aterriza donde está
    def aterrizar(self):
        alturaSuelo=self.controladorDron.getDistanciaSuelo()
        self.controladorDron.down(alturaSuelo-10)
    def bajar(self, distancia, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def irIzquierda(self, velocidad):
        raise NotImplementedError( "Should have implemented this" )

    def irDerecha(self, velocidad):
        raise NotImplementedError( "Should have implemented this" )
  #hacer función extra para probar funciones


 #jorge
    def encender(self):
        raise NotImplementedError( "Should have implemented this" )

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
    def mirarA(self,punto3D velocidad ):
        raise NotImplementedError( "Should have implemented this" )


# sábado 22 oct

# sábado 29 oct
    def sobreVolar(self, listaPuntos3D):
        raise NotImplementedError( "Should have implemented this" )
    

# sábado 5 nov






