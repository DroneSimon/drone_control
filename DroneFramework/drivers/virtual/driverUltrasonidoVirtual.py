_autor_ = "Jorge R. Encinas"
import os
from time import sleep

from DroneFramework.drivers.driver import Driver
from DroneFramework.drivers.virtual.sensorVirtual import SensorVirtual


class DriverUltrasonicoVirtual(Driver):
    def __init__(self):
        self.file = 'sensorUltrasonico.gpio.serial'
        self.file = os.path.join(os.getcwd(), 'DroneFramework', 'drivers','virtual', self.file)
        self.SensorVirtual = SensorVirtual(SensorVirtual.ULTRASONIC, self.file)
        # self.sensorVirtual = SensorVirtual('ultrasonico', file)
        try:
            self.SensorVirtual.start()
        except KeyboardInterrupt:
            if self.SensorVirtual.getRunStatus():
                self.SensorVirtual.stop()
        print 'mode virtual sensor: Magnetometer is runing'

    def getData(self):
        return {'altura' : self.SensorVirtual.getData()}

    def getStatus(self):
        # tiene los datos del sensor
        # ok, no_ok, excepcion,
        raise NotImplementedError("Should have implemented this")

    def forceRead(self):
        # fuerza a hacer una nueva lectura al sensor
        raise NotImplementedError("Should have implemented this")

    def reset(self):
        # inicializa datos sensor
        self.SensorVirtual.stop()
        sleep(.1)
        self.SensorVirtual = SensorVirtual(SensorVirtual.ULTRASONIC, self.file)
        self.SensorVirtual.start()

    def stop(self):
        self.SensorVirtual.stop()
