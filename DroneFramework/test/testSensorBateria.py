import unittest
from drivers.driver import Driver
from hal.sensorBateria import SensorBateria


data = {'nivel' : 100}
status = 'ok'

class DriverBateriaMock(Driver):

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

class SensorBateriaTest(unittest.TestCase):

    def setUp(self):

        self.sensorBateria = SensorBateria(DriverBateriaMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorBateria.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorBateria.getStatus())

    def test_getNivel(self):

        sensorBateria = self.sensorBateria
        esperado = data['nivel']
        self.assertEquals(sensorBateria.getNivel(), esperado)