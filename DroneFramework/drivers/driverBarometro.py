#!/usr/bin/python
_autor_ = "Jorge R. Encinas"
from time import sleep

from deviceMonitor import I2Cscanner
from driver import Driver

NO_PRESENT = 0
OK = 1


class DriverBarometro(Driver):
    def __init__(self):
        self.status = NO_PRESENT
        self.device = I2Cscanner().getDevices()['barometro']
        # print self.device
        # print len(self.device)
        if len(self.device) > 0:  # uno o mas sensores detectados del mismo tipo.
            self.status = OK
            self.device = [self.device[0]]  # force 1 device
            self.oversampling_setting = 1
            self.wait_time = [0.0045, 0.0075, 0.0135, 0.0255]
            self.address_data = 0xF4
            self.AC1 = list()
            self.AC2 = list()
            self.AC3 = list()
            self.AC4 = list()
            self.AC5 = list()
            self.AC6 = list()
            self.B1 = list()
            self.B2 = list()
            self.MB = list()
            self.MC = list()
            self.MD = list()
            # self.UT = list()
            # self.UP = list()
            self.setup()
            self.data = None

    def setup(self):
        for device in self.device:
            bus = device[0]
            address = device[1]
            self.AC1.append(self.read_data_16(bus, address, 0xAA))
            self.AC2.append(self.read_data_16(bus, address, 0xAC))
            self.AC3.append(self.read_data_16(bus, address, 0xAE))
            self.AC4.append(self.read_data_16(bus, address, 0xB0))
            self.AC5.append(self.read_data_16(bus, address, 0xB2))
            self.AC6.append(self.read_data_16(bus, address, 0xB4))
            self.B1.append(self.read_data_16(bus, address, 0xB6))
            self.B2.append(self.read_data_16(bus, address, 0xB8))
            self.MB.append(self.read_data_16(bus, address, 0xBA))
            self.MC.append(self.read_data_16(bus, address, 0xBC))
            self.MD.append(self.read_data_16(bus, address, 0xBE))
        print self.AC1,self.AC2,self.AC3,self.AC4,self.AC5,self.AC6, \
            self.B1, self.B2, self.MB, self.MC, self.MD

    def read_data_16(self, bus, address, adr):
        if self.status is OK:
            msb = bus.read_byte_data(address, adr)
            lsb = bus.read_byte_data(address, adr + 1)
            val = (msb << 8) + lsb
            return val
        else:
            return None

    def read_data_24(self, bus, address, adr):
        if self.status is OK:
            msb = bus.read_byte_data(address, adr)
            lsb = bus.read_byte_data(address, adr + 1)
            xlsb = bus.read_byte_data(address, adr + 2)
            val = ((msb << 16) + (lsb << 8) + xlsb) >> (8 - self.oversampling_setting)
            return val
        else:
            return None

    def prepare(self, bus, address, data):
        if self.status is OK:
            bus.write_byte_data(self, address, self.address_data, data)
            sleep(self.wait_time[self, self.oversampling_setting])
        else:
            return None

    def read_raw_baromether(self):
        data = dict()
        for device in self.device:  # times detect
            bus = device[0]
            address = device[1]
            self.prepare(bus, address, 0x2E)
            temp_out = self.read_data_16(bus, address, 0xF6)
            self.prepare(bus, address, (0x34 + (self.oversampling_setting << 6)))
            presure_out = self.read_data_24(bus, address, 0xF6)
            data.setdefault('bar_raw_temp', []).append(temp_out)
            data.setdefault('bar_raw_presion', []).append(presure_out)
        self.data = self.raw_to_data(data)

    def raw_to_data(self, data):
        # print data
        datos = len(data[data.keys()[0]])
        prom_temp = 0
        prom_pres = 0
        presure = 0
        for temp, presion, i in zip(data['bar_raw_temp'], data['bar_raw_presion'], range(datos)):
            # print temp, self.AC6[i], self.AC5[i], self.MC[i], self.MD[i]
            # print self.B2[i], self.AC2[i], self.AC1[i], self.AC3[i], self.B1[i], self.AC4[i], presion
            # print self.calcule_temp(27769, 19717, 25026, 54461, 2432)
            b5, temp = self.calcule_temp(temp, self.AC6[i], self.AC5[i], self.MC[i], self.MD[i])
            presure = self.calcule_presure(b5, self.B2[i], self.AC2[i], self.AC1[i], self.AC3[i], self.B1[i],
                                           self.AC4[i], presion)

            # prom_temp += temp
            # prom_pres += presure
            # prom_temp /= datos
            # prom_pres /= datos
        data.setdefault('bar_temp', prom_temp)
        data.setdefault('bar_presion', prom_pres)
        self.printData(data)
        return data

    def printData(self, data):
        print data

    def calcule_temp(self, ut, ac6, ac5, mc, md):
        x1 = ((ut - ac6) * ac5) >> 15
        print 'x1=', x1,
        x2 = (mc << 11) / (x1 + md)
        print 'x2=', x2,
        b5 = x1 + x2
        print 'b5=', b5,
        print 't=', ((b5 + 8) >> 4) / 10.0,
        return (b5, (((b5 + 8) >> 4) / 10.0))

    def calcule_presure(self, b5, b2, ac2, ac1, ac3, b1, ac4, up):
        b6 = b5 - 4000
        x1 = (b2 * (b6 * b6) >> 12) >> 11
        x2 = (ac2 * b6) >> 11
        x3 = x1 + x2
        b3 = (((ac1 * 4 + x3) << self.oversampling_setting) + 2) / 4
        x1 = (ac3 * b6) >> 13
        x2 = (b1 * ((b6 * b6) >> 12)) >> 16
        x3 = ((x1 + x2) + 2) >> 2
        b4 = (ac4 * (x3 + 32768)) >> 15
        b7 = (up - b3) * (50000 >> self.oversampling_setting)
        if b7 < 0x80000000:
            p = (b7 * 2) / b4
        else:
            p = (b7 / b4) * 2
        x1 = (p >> 8) * (p >> 8)
        x1 = (x1 * 3038) >> 16
        x2 = (-7357 * p) >> 16
        return p + ((x1 + x2 + 3791) >> 4)

    def getData(self):
        if self.status is OK:
            self.read_raw_baromether()
            # # return self.data
            # data = dict()
            # data['angulo'] = self.data['angulo']
            return self.data

    def getStatus(self):
        return self.status

    def forceRead(self):
        return {'angulo': degrees(self.data)}

    def reset(self):
        print 'verificando presencia del sensor'
        # reconform sensor ['Giroscipio'] in bus is present or presents
        # setup()


def test():
    # from time import sleep
    barometro = DriverBarometro()


    # # for i in range(0, 100):
    # barometro.getData()
    # sleep(.1)


if __name__ == "__main__":
    try:
        test()
    except KeyboardInterrupt:
        pass
