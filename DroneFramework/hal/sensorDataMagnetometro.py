from drivers.driver import Driver
from sensorData import SensorData

__author__ = 'Diego Garcia'


class SensorDataMagnetometro(SensorData):

    def __init__(self, data, age):
        """
        :type driver Driver
        """

        #sensorData = {angulo : 0}
        self.data = data
        self.age = age

    def getData(self):

        return self.data

    def getAge(self):

        return self.age

    def setData(self, data):

        self.data = data

    def setAge(self, age):

        self.age = age

