import unittest
from hal.sensorDataUltrasonido import SensorDataUltrasonido
from datetime import *


data = {'altura': 200}


class SensorDataUltrasonidoTest(unittest.TestCase):

    def setUp(self):

        self.dataUltrasonido = SensorDataUltrasonido(data, datetime.today())

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.dataUltrasonido.getData())

    def test_getData(self):

        self.assertEquals(self.dataUltrasonido.getData(), data)

    def test_setData(self):

        dataUltrasonido = self.dataUltrasonido
        new_data = {'altura': 50}
        dataUltrasonido.setData(new_data)
        self.assertEquals(dataUltrasonido.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataUltrasonido.getData())

    def test_setAge(self):

        dataUltrasonido = self.dataUltrasonido
        new_age = datetime.today()
        dataUltrasonido.setAge(new_age)
        self.assertEquals(dataUltrasonido.getAge(), new_age)