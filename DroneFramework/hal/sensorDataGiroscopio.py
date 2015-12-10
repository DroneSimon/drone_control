from sensorData import SensorData
from drivers.driver import Driver


__author__ = 'Diego Garcia'


class SensorDataGiroscopio(SensorData):

    def __init__(self, data, age):
        """
        :type driver Driver
        """
        #data = {'x': 0, 'y': 0, 'z': 0, 'inclinacion_x': 0, 'inclinacion_y' : 0}
        self.data = data
        self.age = age

    def getData(self):
        # tiene los datos del sensor
        return self.data

    def getAge(self):
        # tiene los datos del sensor
        return self.age

    def setData(self, data):

        self.data = data

    def setAge(self, age):

        self.age = age