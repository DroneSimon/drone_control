import unittest
from DroneFramework.hal.sensorDataMagnetometro import SensorDataMagnetometro
from datetime import *

class SensorDataMagnetometroTest(unittest.TestCase):

    def setUp(self):
        self.data = {'angulo': 90}

        self.dataMagnometro = SensorDataMagnetometro(data, datetime.today())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_getData(self):

        self.assertEquals(self.dataMagnometro.getData(), data)

    def test_setData(self):

        dataMagnetometro = self.dataMagnometro
        new_data = {'angulo': 50}
        dataMagnetometro.setData(new_data)
        self.assertEquals(dataMagnetometro.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataMagnometro.getData())

    def test_setAge(self):

        dataMagnetometro = self.dataMagnometro
        new_age = datetime.today()
        dataMagnetometro.setAge(new_age)
        self.assertEquals(dataMagnetometro.getAge(), new_age)