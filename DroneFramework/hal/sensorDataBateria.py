from sensorData import SensorData
from DroneFramework.drivers.driver import Driver

__author__ = 'Diego Garcia'


class SensorDataBateria(SensorData):

    def __init__(self, data, age):
        """
        :type driver Driver
        """
        #data = {'nivel': 0}
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