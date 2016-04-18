import unittest
from DroneFramework.hal.sensorDataBateria import SensorDataBateria
from datetime import *


data = {'nivel': 40}

class SensorDataBateriaTest(unittest.TestCase):

    def setUp(self):

        self.dataBateria = SensorDataBateria(data, datetime.today())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataBateria.getData())

    def test_getData(self):

        self.assertEquals(self.dataBateria.getData(), data)

    def test_setData(self):

        dataBateria = self.dataBateria
        new_data = {'nivel': 50}
        dataBateria.setData(new_data)
        self.assertEquals(dataBateria.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataBateria.getData())

    def test_setAge(self):

        dataBateria = self.dataBateria
        new_age = datetime.today()
        dataBateria.setAge(new_age)
        self.assertEquals(dataBateria.getAge(), new_age)