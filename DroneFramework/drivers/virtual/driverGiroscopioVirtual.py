_autor_ = "Jorge R. Encinas"
import os
from time import sleep

from DroneFramework.drivers.driver import Driver
from DroneFramework.drivers.virtual.sensorVirtual import SensorVirtual


class DriverGiroscopioVirtual(Driver):
    def __init__(self):
        self.file = 'sensorGiroscopio.i2c.serial'
        self.file = os.path.join(os.getcwd(), 'DroneFramework', 'drivers','virtual', self.file)
        self.SensorVirtual = SensorVirtual(SensorVirtual.GYROSCOPE, self.file)
        # self.SensorVirtual = SensorVirtual("giroscopio", self.file)
        try:
            self.SensorVirtual.start()
        except KeyboardInterrupt:
            if self.SensorVirtual.getRunStatus():
                self.SensorVirtual.stop()
        print 'mode virtual sensor: Gyroscope is runing'

    def getData(self):
        giroscopio = self.SensorVirtual.getData()
        data = dict()
        data['inclinacion_x'] = giroscopio[12]
        data['inclinacion_y'] = giroscopio[13]

        #ojo jorge implementar esto para que corra prueba de pitch
        data['x'] = giroscopio[0] #(gyro_xout / 131) #scaled
        data['y'] = giroscopio[1] #(gyro_yout / 131) #scaled
        data['z'] = giroscopio[2] #(gyro_zout / 131) #scaled


        return data

    def getStatus(self):
        # tiene los datos del sensor
        # ok, no_ok, excepcion,
        return 'ok'

    def forceRead(self):
        # fuerza a hacer una nueva lectura al sensor
        return self.getData()

    def reset(self):
        # inicializa datos sensor
        self.SensorVirtual.stop()
        sleep(.1)
        self.SensorVirtual = SensorVirtual(SensorVirtual.GYROSCOPE, self.file)
        self.SensorVirtual.start()

    def stop(self):
        self.SensorVirtual.stop()
