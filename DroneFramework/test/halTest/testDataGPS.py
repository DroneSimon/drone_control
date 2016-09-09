import unittest
from hal.sensorDataGPS import SensorDataGPS
from datetime import *


data = {'latitud': 543, 'longitud': 345, 'altitud': 656}


class SensorDataGPSTest(unittest.TestCase):

    def setUp(self):

        self.dataGPS = SensorDataGPS(data, datetime.today())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataGPS.getData())

    def test_getData_Latitud(self):

        self.assertEquals(self.dataGPS.getData()['latitud'], data['latitud'])

    def test_getData_Longitud(self):

        self.assertEquals(self.dataGPS.getData()['longitud'], data['longitud'])

    def test_getData_altitud(self):

        self.assertEquals(self.dataGPS.getData()['altitud'], data['altitud'])

    def test_getData(self):

        self.assertEquals(self.dataGPS.getData(), data)

    def test_setData(self):
        dataGPS = self.dataGPS
        new_data = {'latitud': 234, 'longitud': 178, 'altitud': 756}
        dataGPS.setData(new_data)
        self.assertEquals(dataGPS.getData(), new_data)


    def test_getAge(self):
        self.assertIsNotNone(self.dataGPS.getData())

    def test_setAge(self):
        dataGPS = self.dataGPS
        new_age = datetime.today()
        dataGPS.setAge(new_age)
        self.assertEquals(dataGPS.getAge(), new_age)
