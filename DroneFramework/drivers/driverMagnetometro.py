#!/usr/bin/python
_autor_ = "Jorge R. Encinas"
import math

from deviceMonitor import I2Cscanner
from driver import Driver

NO_PRESENT = 0
OK = 1


class DriverMagnetometro(Driver):
    def __init__(self):
        self.status = NO_PRESENT
        self.device = I2Cscanner().getDevices()['magnetometro']
        # self.device = [self.device[0]]  # force 1 device
        print self.device
        print len(self.device)
        if len(self.device) > 0:  # uno o mas sensores detectados del mismo tipo.
            self.status = OK
            self.scale = 0.92  # from gauss 1.3
            self.samples = 0b01110000  # Set to 8 samples @ 15Hz 0 11 100 00
            self.gauss = 0b00100000  # 1.3 gain LSb / Gauss 1090 (default) 0001
            self.sampling = 0b00000000  # Continuous sampling
            self.setup()
            self.data = None

    def setup(self):
        for device in self.device:
            bus = device[0]
            address = device[1]
            bus.write_byte_data(address, 0, self.samples)
            bus.write_byte_data(address, 1, self.gauss)
            bus.write_byte_data(address, 2, self.sampling)

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
        self.data = dict()
        for device in self.device:
            bus = device[0]
            address = device[1]
            x_out, y_out, z_out = self.read_raw(address, bus)
            scale_y, scale_x = self.interpretData(self.data, x_out, y_out, z_out)
            heading = math.atan2(scale_y, scale_x)
            if heading < 0:
                heading += 2 * math.pi
            self.data.setdefault('radian', []).append(heading)
            self.data.setdefault('angulo', []).append(math.degrees(heading))
            # self.data = self.interpretData(data)

    def interpretData(self, data, x_out, y_out, z_out):
        data.setdefault('raw_mag_x', []).append(x_out)  # 'x'
        scale_x = x_out * self.scale
        data.setdefault('mag_x', []).append(scale_x)  # 'x'
        data.setdefault('raw_mag_y', []).append(y_out)  # 'y'
        scale_y = y_out * self.scale
        data.setdefault('mag_y', []).append(scale_y)  # 'y'
        data.setdefault('raw_mag_z', []).append(z_out)  # 'z'
        data.setdefault('mag_z', []).append(z_out * self.scale)  # 'z'
        return scale_y, scale_x

    def read_raw(self, address, bus):
        x_out = self.read_data_bus(bus, address, 3)
        y_out = self.read_data_bus(bus, address, 5)
        z_out = self.read_data_bus(bus, address, 7)
        return x_out, y_out, z_out

    # def interpretData(self, data):
    #     tamanoEjes = len(data[data.keys()[0]])
    #     for ejes in data:
    #         promedio = 0
    #         for eje in data[ejes]:
    #             promedio += eje
    #         promedio /= tamanoEjes
    #         data[ejes] = promedio * self.scale
    #     heading = math.atan2(data['y'], data['x'])
    #     if heading < 0:
    #         heading += 2 * math.pi
    #     data.setdefault('radian', heading)
    #     data.setdefault('angulo', math.degrees(heading))
    #     return data

    def getData(self):
        if self.status is OK:
            self.read_xyz()
            # return self.data
            data = dict()
            data['norte'] = self.data['angulo']
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
    magnetometro = DriverMagnetometro()
    for i in range(0, 100):
        print magnetometro.getData()
        sleep(.1)


if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        pass
