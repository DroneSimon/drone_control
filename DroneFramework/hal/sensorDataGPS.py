from drivers.driver import Driver
from sensorData import SensorData

__author__ = 'Diego Garcia'


class SensorDataGPS(SensorData):

    def __init__(self, data, age):
        """
        :type driverGPS Driver
        """

        # sensorData es un diccionario
        # sensorData = {'latitud : 0, longitud : 0, altitud:0'}
        self.data = data
        #age contiene la fecha y la hora
        self.age = age

    def getData(self):
        return self.data

    def getAge(self):
        return self.age

    def setData(self, data):
        self.data = data

    def setAge(self, age):
        self.age = age