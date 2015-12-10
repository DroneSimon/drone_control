__author__ = 'Diego Garcia'

from DroneFramework.drivers.driver import Driver
from sensor import Sensor
from sensorDataMagnetometro import SensorDataMagnetometro

from datetime import *

class SensorMagnetometro(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        self.sensorData = SensorDataMagnetometro(driver.getData(),datetime.today())
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData

    def getStatus(self):

        return self.status

    def reset(self):

        self.driver.reset()

    def forceRead(self):

        self.driver.forceRead()

    def getAnguloCabezaDron(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())

        return self.sensorData.getData()['angulo']