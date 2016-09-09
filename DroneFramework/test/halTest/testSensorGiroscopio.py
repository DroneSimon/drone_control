import unittest
from DroneFramework.drivers.driver import Driver
from DroneFramework.hal.sensorGiroscopio import SensorGiroscopio


data = {'x': 1, 'y': 6, 'z': 3, 'inclinacion_x' : 90, 'inclinacion_y' : 180}
status = 'ok'

class DriverGiroscopioMock(Driver):

    def __init__(self):

        self.data = data
        self.status = status

    def getData(self):

        return self.data

    def getStatus(self):

        return self.status

    def forceRead(self):

        raise NotImplementedError( "Should have implemented this" )

    def reset(self):

        raise NotImplementedError( "Should have implemented this" )

class SensorGiroscopioTest(unittest.TestCase):

    def setUp(self):

        self.sensorGiroscopio = SensorGiroscopio(DriverGiroscopioMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.getStatus())

    def test_verPosicion_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.verPosicion())

    def test_verPosicion(self):

        sensorGiroscopio = self.sensorGiroscopio
        esperado = (data['x'], data['y'], data['z'])
        self.assertEquals(sensorGiroscopio.verPosicion(), esperado)

    def test_verInclinacion_NoNone(self):

        self.assertIsNotNone(self.sensorGiroscopio.verInclinacion())

    def test_verInclinacion(self):

        sensorGiroscopio = self.sensorGiroscopio
        esperado = (data['inclinacion_x'], data['inclinacion_y'])
        self.assertEquals(sensorGiroscopio.verInclinacion(), esperado)


