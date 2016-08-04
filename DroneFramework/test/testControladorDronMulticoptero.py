#!/usr/bin/python
_autor_ = "Jorge R. Encinas"

import unittest

from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero


class TestControladorDronMulticoptero(unittest.TestCase):
    def setUp(self):
        self.controlador = ControladorDronMulticoptero()


# encender equivale a decir armar motores en OP
class testEnceder(TestControladorDronMulticoptero):
    def runTest(self):
        self.controlador.actuadorOP.writeSerial('STATE')
        self.assertEquals(self.controlador.actuadorOP.status, 'OK')


# lee la altidud actual del GPS y setea ese valor variable de clase
class testSetAltitudSuelo(TestControladorDronMulticoptero)
    def runTest(self):
        self.controlador.setAltitudSuelo()
        # crear rango de tolerancia
        self.assertEquals(self.controlador.altitudSuelo, self.controlador.sensorGPS.getLastInfo().getData()['altitud'])


# apagar equivale a decir que desarme motores en OP
class testApagar(TestControladorDronMulticoptero):
    def runTest(self):
        self.controlador.apagar()
        self.assertEquals(self.controlador.actuadorOP.getThrottle(), 0)


# giro lateral de la cabeza desde la pocision donde esta
# velocidad es un entero de 1 al 50, no puede ser 0
# si grados es negativo ira a la izquierda, sino a la derecha
# para esta funcionalidad se asumió que si velocidad mayor a 50 va a la derecha
# para esta funcionalidad se asumió que si velocidad menor a 50 va a la izquierda
class testYaw(TestControladorDronMulticoptero):
    def runTest(self):
        self.controlador.yaw(90, 20)
        # se ha considerado una tolerancia del +-0.5% en grados
        self.assertEquals(self.controlador.sensorMagnetometro.getLastInfo(), 90)


# giro lateral de la cabeza a la izquierda desde la posicion donde esta
class testYaw_izquierda(TestControladorDronMulticoptero):
    def runTest(self):
        yaw = self.controlador.actuadorOP.getYaw()
        self.controlador.yaw_izquierda((yaw - 10), 20)
        self.assertEquals(self.controlador.actuadorOP.getYaw(), yaw - 10)


# giro lateral de la cabeza a la derecha desde la pocision donde esta
class testYaw_derecha(TestControladorDronMulticoptero):
    def runTest(self):
        yaw = self.controlador.actuadorOP.getYaw()
        self.controlador.yaw_derecha((yaw + 10), 20)
        self.assertEquals(self.controlador.actuadorOP.getYaw(), yaw + 10)


# elevar el dron: distancia estará en centimetros y es la distancia que debe subir desde donde esta
# velocidad para elevarse debe ser mayor a velocidadEstable y menor a velocidadMaxMotores
# velocidad se sumara a la velocidad estable - hasta velocidadMaxMotores

class testUp(TestControladorDronMulticoptero):
    def runTest(self):
        altura = self.controlador.sensorUltrasonido.getAltura()
        # si es mayor a la maxima altura del ultrasonico o fuera de alcance, tomar la altitud del gps.
        self.controlador.up(altura + 20, 10)
        self.assertEquals(self.controlador.sensorUltrasonido.getAltura(), altura + 20)


# bajar el dron hasta "distancia" del piso. Estara en centimetros
# velocidad tendria que ser menor a la estable si es mayor la dejo en velocidad estable, e.d. no baja
class testDown(TestControladorDronMulticoptero):
    def runTest(self):
        altura = self.controlador.sensorUltrasonido.getAltura()
        # si es mayor a la maxima altura del ultrasonico o fuera de alcance, tomar la altitud del gps.
        self.controlador.up(altura - 20, 10)
        self.assertEquals(self.controlador.sensorUltrasonido.getAltura(), altura - 20)


# me devuelve la distancia del dron al suelo, si esta fuera del alcance del ultrasonido devuelve
# distancia GPS. para ello se debera setear 1ro distancia altitud suelo
class testGetDistanciaSuelo(TestControladorDronMulticoptero):
    def runTest(self):
        altura = self.controlador.sensorUltrasonido.getAltura()
        self.assertTrue(altura > 0)
        self.assertTrue(altura < 4000)


# método de aterrizar velocidad 30-10-5
class testAterrizar1(TestControladorDronMulticoptero):
    def runTest(self):
        self.controlador.aterrizar1()
        throttle = self.controlador.actuadorOP.getThrottle()
        self.assertTrue(throttle is 30)
        throttle = self.controlador.actuadorOP.getThrottle()
        self.assertTrue(throttle is 10)
        throttle = self.controlador.actuadorOP.getThrottle()
        self.assertTrue(throttle is 5)


# metodo aterrizar bajando gradualmente la velocidad
class testAterrizar2(TestControladorDronMulticoptero):
    def runTest(self):
        self.controlador.aterrizar2()
        throttle = self.controlador.actuadorOP.getThrottle()
        raise ( 'controlar la velocidad de bajada' )
