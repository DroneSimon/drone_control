from drivers.driver import Driver
from sensor import Sensor
from sensorDataBateria import SensorDataBateria
from datetime import *


#modified by Diego Garcia
class SensorBateria(Sensor):

    def __init__(self, driver):
        """
        :type driver Driver
        """
        self.sensorData = SensorDataBateria(driver.getData(), datetime.today())
        self.status = driver.getStatus()
        self.driver = driver

    def getLastInfo(self):

        self.actualizarData()
        return self.sensorData

    def getStatus(self):

        return self.status

    def reset(self):

        self.driver.reset()

    def forceRead(self):

        self.driver.forceRead()

    def getNivel(self):

        self.actualizarData()
        return self.sensorData.getData()['nivel']

    def actualizarData(self):

        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())