from capaDronAltoNivel.dronVolador import DronVolador
from capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero

from scipy.spatial import distance


class DronMulticoptero (DronVolador):

    def __init__(self,controladorMulticoptero):
        """
        :type controladorMulticoptero: ControladorDronMulticoptero
        """
        # inicializa controladorDron, puntoPartida, posicionActual, modo, encendido
        DronVolador.__init__(controladorMulticoptero)

    # Aterriza donde está
    def aterrizar(self):
        alturaSuelo=self.controladorDron.getDistanciaSuelo()
        self.controladorDron.down(alturaSuelo-10)



    def orbitar(self,centro, radio):
        raise NotImplementedError( "Should have implemented this" )

    def bajar(self, distancia):
        raise NotImplementedError( "Should have implemented this" )

    def sobrevolar(self, listaPuntos3D):
        raise NotImplementedError( "Should have implemented this" )

    def subir(self, distancia):
        raise NotImplementedError( "Should have implemented this" )

    # dirige la cabeza al punto XYZ
    def mirarA(self, puntoXYZ):
        raise NotImplementedError( "Should have implemented this" )



