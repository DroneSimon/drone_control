import unittest
from datetime import *
from hal.sensorDataGiroscopio import SensorDataGiroscopio


data = {'x': 1, 'y': 6, 'z': 3, 'angulo' : 90}


class SensorDataGiroscopioTest(unittest.TestCase):

    def setUp(self):
        self.dataGiroscopio = SensorDataGiroscopio(data, datetime.today())

    def test_getData_NoNone(self):
        self.assertIsNotNone(self.dataGiroscopio.getData())

    def test_getData_X(self):
        self.assertEquals(self.dataGiroscopio.getData()['x'], data['x'])

    def test_getData_Y(self):
        self.assertEquals(self.dataGiroscopio.getData()['y'], data['y'])

    def test_getData_Z(self):
        self.assertEquals(self.dataGiroscopio.getData()['z'], data['z'])

    def test_getData_Angulo(self):
        self.assertEquals(self.dataGiroscopio.getData()['angulo'], data['angulo'])

    def test_getData(self):
        self.assertEquals(self.dataGiroscopio.getData(), data)

    def test_setData(self):
        dataGiroscopio = self.dataGiroscopio
        new_data = {'x': 4, 'y': 7, 'z': 6, 'angulo' : 50}
        dataGiroscpio.setData(new_data)
        self.assertEquals(dataGiroscopio.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataGiroscopio.getData())

    def test_setAge(self):

        dataGiroscopio = self.dataGiroscopio
        new_age = datetime.today()
        dataGiroscopio.setAge(new_age)
        self.assertEquals(dataGiroscopio.getAge(), new_age)