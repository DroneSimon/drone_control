__author__ = 'Diego Garcia'
# modificado I.C.C

from DroneFramework.drivers.driver import Driver
from sensor import Sensor
from sensorDataUltrasonido import SensorDataUltrasonido

from datetime import *

class SensorUltrasonido(Sensor):

    def __init__(self, driver, alcance):
        """
        :type driver: Driver
        """
        # age= datetime.today() guarda la fecha y la hora de la ultima lectura del sensor
        self.sensorData = SensorDataUltrasonido(driver.getData(), datetime.today())
        self.status = driver.getStatus()
        self.driver = driver
        self.alcance = alcance


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

    #al llamar driver.getData se obliga a leer al driver
    def getAltura(self):
        self.sensorData.setData(self.driver.getData())
        self.sensorData.setAge(datetime.today())
        return self.sensorData.getData()['altura']

    #devuelve el alcance maximo del ultrasonido si 0 es que esta en el piso
    # si esta en el maximo puede estar mas de  el maximo
    def getAlcance(self):
        return self.alcance
