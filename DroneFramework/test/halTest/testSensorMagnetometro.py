import unittest
from drivers.driver import Driver
from hal.sensorMagnetometro import SensorMagnetometro


data = {'angulo' : 120}
status = 'ok'

class DriverMagnetometroMock(Driver):

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

class SensorMagnetometroTest(unittest.TestCase):

    def setUp(self):

        self.sensorMagnetometro = SensorMagnetometro(DriverMagnetometroMock())

    def test_getLastInfo_NoNone(self):

        self.assertIsNotNone(self.sensorMagnetometro.getLastInfo())

    def test_getEstado_NoNone(self):

        self.assertIsNotNone(self.sensorMagnetometro.getStatus())

    def test_getAltura(self):

        self.assertEquals(self.sensorMagnetometro.getAnguloCabezaDron(), data['angulo'])


