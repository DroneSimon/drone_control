import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta
#from capaDronBajoNivel.controladorDron import ControladorDron
#from capaDronBajoNivel.controladorDronVolador import ControladorDronVolador

#from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDron
from DroneFramework.capaDronBajoNivel.controladorDronVolador import ControladorDronVolador
#from DroneFramework.capaDronAltoNivel.dronMulticoptero import DronMulticoptero


from dron import Dron
from scipy.spatial import distance


class DronVolador (Dron):
    __metaclass__ = ABCMeta

    def __init__(self,controladorDronVolador):
        """
         :type controladorDronVolador: ControladorDronVolador
        """
        # inicializa
        Dron.__init__(self, controladorDronVolador)


    def aterrizar(self):
        self.controladorDron.aterrizar()


    @abc.abstractmethod
    def orbitar(self,centro, radio):
        raise NotImplementedError( "Should have implemented this" )


    def bajar(self, distancia, velocidad):
        self.controladorDron.down(distancia,velocidad)

    @abc.abstractmethod
    def sobrevolar(self, listaPuntos3D):
        raise NotImplementedError( "Should have implemented this" )


    def subir(self, distancia,velocidad):
        self.controladorDron.up(distancia,velocidad)



