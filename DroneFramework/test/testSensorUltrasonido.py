import unittest
from drivers.driver import Driver
from hal.sensorUltrasonido import SensorUltrasonido


data = {'altura' : 500}
alcance = 10
status = 'ok'

class DriverUltrasonidoMock(Driver):

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

class SensorUltrasonidoTest(unittest.TestCase):

    def setUp(self):
        self.sensorUltrasonido = SensorUltrasonido(DriverUltrasonidoMock(), alcance)

    def test_getLastInfo_NoNone(self):
        self.assertIsNotNone(self.sensorUltrasonido.getLastInfo())

    def test_getEstado_NoNone(self):
        self.assertIsNotNone(self.sensorUltrasonido.getStatus())

    def test_getAltura(self):
        self.assertEquals(self.sensorUltrasonido.getAltura(), data['altura'])

    def test_getAlacance(self):
        self.assertEquals(self.sensorUltrasonido.getAlcance(), alcance)


