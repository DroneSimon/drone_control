import unittest
from drivers.driver import Driver
from hal.sensorGPS import SensorGPS


data = {'latitud': 543, 'longitud': 345, 'altitud': 656}
status = 'ok'

class DriverGPSMock(Driver):

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

class SensorGPSTest(unittest.TestCase):

    def setUp(self):

        self.sensorGPS = SensorGPS(DriverGPSMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorGPS.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorGPS.getStatus())

    def test_getCoordenadas_NoNone(self):

        self.assertIsNotNone(self.sensorGPS.getCoordenadas())

    def test_getCoordenadas(self):

        sensorGPS = self.sensorGPS
        esperado = (data['latitud'], data['longitud'], data['altitud'])
        self.assertEquals(sensorGPS.getCoordenadas(), esperado)