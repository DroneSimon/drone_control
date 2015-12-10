from drivers.driver import Driver
from sensor import Sensor
from sensorDataGiroscopio import SensorDataGiroscopio
from datetime import *

__author__ = 'Diego Garcia'


class SensorGiroscopio(Sensor):

    def __init__(self, driver):
        """
        :type driver: Driver
        """

        self.sensorData = SensorDataGiroscopio(driver.getData(), datetime.today())
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData, luego de leer el driver
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData

    def getStatus(self):
        #devuelve el estado del sensor
        return self.status

    def reset(self):
        #inicializa el sensor
        self.driver.reset()

    def forceRead(self):
        #obliga a leer al sensor
        self.driver.forceRead()

    def verPosicion(self):
        """
        :return: una tupla con un vistaso de la posicion
        """
        self.actualizarData()
        data = self.sensorData.getData()
        return (data['x'], data['y'], data['z'])

    def verInclinacion(self):
        """
        :return: inclinacion x, inclinacion y
        """
        self.actualizarData()
        return (self.sensorData.getData()['inclinacion_x'], self.driver.getData()['inclinacion_y'])

    def actualizarData(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())

