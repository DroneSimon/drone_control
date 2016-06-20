#!/usr/bin/python
_autor_ = "Jorge R. Encinas"
import math

from deviceMonitor import I2Cscanner
from driver import Driver

NO_PRESENT = 0
OK = 1


class DriverGiroscipio(Driver):
    def __init__(self):
        self.status = NO_PRESENT
        self.device = I2Cscanner().getDevices()['giroscopio']
        # self.device = [self.device[0]]  # force only one device
        if len(self.device) > 0:  # uno o mas sensores detectados del mismo tipo.
            self.status = OK
            self.scale_gyro = 131  # from datasheet
            self.scale_accel = 16384.0  # from datasheet
            self.power_mgmt_1 = 0x6b  # Power management registers
            self.power_mgmt_2 = 0x6c  # Power management registers
            self.wake = 0  # wake the 6050 up as it starts in sleep mode
            self.setup()
            self.data = None

    def setup(self):
        for device in self.device:
            bus = device[0]
            address = device[1]
            bus.write_byte_data(address, self.power_mgmt_1, self.wake)

    def read_data_bus(self, bus, address, adr):
        if self.status is OK:
            high = bus.read_byte_data(address, adr)
            low = bus.read_byte_data(address, adr + 1)
            val = (high << 8) + low
            if val >= 0x8000:
                return -((65535 - val) + 1)
            else:
                return val
        else:
            return None

    def read_xyz(self):
        data = dict()
        for device in self.device:
            bus = device[0]
            address = device[1]
            accel_xout, accel_yout, accel_zout, gyro_xout, gyro_yout, gyro_zout, temp_out = self.get_raw(address, bus)
            giro_y, giro_x = self.interpretData(accel_xout, accel_yout, accel_zout, data, gyro_xout, gyro_yout,
                                                gyro_zout, temp_out)
            self.heading(data, giro_x, giro_y)
        self.data = data

    def heading(self, data, giro_x, giro_y):
        heading = math.atan2(giro_y, giro_x)
        if heading < 0:
            heading += 2 * math.pi
        data.setdefault('radian', heading)
        data.setdefault('angulo', math.degrees(heading))

    def interpretData(self, accel_xout, accel_yout, accel_zout, data, gyro_xout, gyro_yout, gyro_zout, temp_out):
        data.setdefault('raw_temp', []).append(temp_out)
        data.setdefault('temp_mpu', []).append(temp_out / 340.00 + 36.53)
        data.setdefault('raw_giro_x', []).append(gyro_xout)
        gyro_x = gyro_xout / self.scale_gyro
        data.setdefault('giro_x', []).append(gyro_x)
        data.setdefault('raw_giro_y', []).append(gyro_yout)
        gyro_y = gyro_yout / self.scale_gyro
        data.setdefault('giro_y', []).append(gyro_y)
        data.setdefault('raw_giro_z', []).append(gyro_zout)
        data.setdefault('giro_z', []).append(gyro_zout / self.scale_gyro)
        data.setdefault('raw_accel_x', []).append(accel_xout)
        data.setdefault('accel_x', []).append(accel_xout / self.scale_accel)
        data.setdefault('raw_accel_y', []).append(accel_yout)
        data.setdefault('accel_y', []).append(accel_yout / self.scale_accel)
        data.setdefault('raw_accel_z', []).append(accel_zout)
        data.setdefault('accel_z', []).append(accel_zout / self.scale_accel)
        return gyro_y, gyro_x

    def get_raw(self, address, bus):
        temp_out = self.read_data_bus(bus, address, 0x41)
        gyro_xout = self.read_data_bus(bus, address, 0x43)
        gyro_yout = self.read_data_bus(bus, address, 0x45)
        gyro_zout = self.read_data_bus(bus, address, 0x47)
        accel_xout = self.read_data_bus(bus, address, 0x3b)
        accel_yout = self.read_data_bus(bus, address, 0x3d)
        accel_zout = self.read_data_bus(bus, address, 0x3f)
        return accel_xout, accel_yout, accel_zout, gyro_xout, gyro_yout, gyro_zout, temp_out

    def getData(self):
        if self.status is OK:
            # return self.data
            self.read_xyz()
            data = dict()
            data.setdefault('angulo_xy', []).append(self.data['giro_x'])
            data.setdefault('angulo_xy', []).append(self.data['giro_y'])
            return data

    def getStatus(self):
        return self.status

    def forceRead(self):
        return {'angulo': math.degrees(self.data)}

    def reset(self):
        print 'verificando presencia del sensor'
        # reconform sensor ['Giroscipio'] in bus is present or presents
        # setup()


def test():
    from time import sleep
    giroscopio = DriverGiroscipio()
    for i in range(0, 100):
        print giroscopio.getData()
        sleep(.1)


if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        pass
