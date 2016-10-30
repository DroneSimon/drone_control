from DroneFramework.drivers.driver import Driver
from sensor import Sensor
from sensorDataGPS import SensorDataGPS

from datetime import *

class SensorGPS(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """

        self.sensorData = SensorDataGPS(driver.getData(), datetime.today())
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData

    def getStatus(self):
        return self.driver.getStatus()

    def reset(self):
        self.driver.reset()

    def forceRead(self):
        self.driver.forceRead()
        self.getCoordenadas()

    def getCoordenadas(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        data = self.sensorData.getData()
        return (data)