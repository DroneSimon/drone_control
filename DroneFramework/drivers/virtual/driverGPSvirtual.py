_autor_ = "Jorge R. Encinas"
import os
from time import sleep

from DroneFramework.drivers.driver import Driver
from DroneFramework.drivers.virtual.sensorVirtual import SensorVirtual


class DriverGPSvirtual(Driver):
    def __init__(self):
        self.file = 'gpsDataCaptured.serial'
        self.file = os.path.join(os.getcwd(), 'DroneFramework', 'drivers','virtual', self.file)
        self.SensorVirtual = SensorVirtual(SensorVirtual.GPS, self.file)
        # self.SensorVirtual = SensorVirtual("gps", self.file)
        try:
            self.SensorVirtual.start()
        except KeyboardInterrupt:
            if self.SensorVirtual.getRunStatus():
                self.SensorVirtual.stop()
        print 'mode virtual sensor: GPS is runing'

    def getData(self):
        gps = self.SensorVirtual.getData()
        data = dict()
        data['latitud'] = gps[0]
        data['longitud'] = gps[1]
        data['altitud'] = gps[2]
        return data

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
        self.SensorVirtual = SensorVirtual(SensorVirtual.GPS, self.file)
        self.SensorVirtual.start()

    def stop(self):
        self.SensorVirtual.stop()
