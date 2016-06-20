from smbus import SMBus

PWM = 'pwm'

BAROMETRO = 'barometro'

MAGNETOMETRO = 'magnetometro'

ACELEROMETRO = 'acelerometro'

GIROSCOPIO = 'giroscopio'

OTRO = 'otros'


# asumiendo raspberry pi 2
# pendiente para revision y mejora
class I2Cscanner():
    endAddress = 0x77
    startAddress = 0x00
    ModuleBMP085 = 0x77
    ModuleMPU6050 = 0x68
    ModulePCA9685 = 0x40
    ModuleHMC5883L = 0x1E
    devices = dict()
    scanned = False
    bus = list()
    bus.append(SMBus(0))  # pendiente para revision y mejora
    bus.append(SMBus(1))  # pendiente para revision y mejora

    def scanDevices(self):
        if not I2Cscanner.scanned:
            for bus in self.bus:
                for address in range(self.startAddress, self.endAddress + 1):
                    try:
                        bus.read_byte(address)
                        self.addDevice(bus, address)
                    except IOError:
                        pass
        I2Cscanner.scanned = True

    def addDevice(self, bus, address):
        if address is self.ModuleMPU6050:
            I2Cscanner.devices.setdefault(GIROSCOPIO, list()).append([bus, address])
            I2Cscanner.devices.setdefault(ACELEROMETRO, list()).append([bus, address])
        elif address is self.ModuleHMC5883L:
            I2Cscanner.devices.setdefault(MAGNETOMETRO, list()).append([bus, address])
        elif address is self.ModuleBMP085:
            I2Cscanner.devices.setdefault(BAROMETRO, list()).append([bus, address])
        elif address is self.ModulePCA9685:
            I2Cscanner.devices.setdefault(PWM, list()).append([bus, address])
        else:
            I2Cscanner.devices.setdefault(OTRO, list()).append([bus, address])

    def getDevices(self):
        if not I2Cscanner.scanned:
            self.scanDevices()
        return I2Cscanner.devices

    def printDevices(self):
        for bus in I2Cscanner.devices.items():
            print bus

    def forceGetDevices(self):
        I2Cscanner.scanned = False
        return self.getDevices()

    class GPIOscanner:
        GPIO_TRIGGER = 22;
        GPIO_ECHO = 18


def test():
    d1 = I2Cscanner()
    print d1.devices, ;
    print d1.scanned
    d1.scanDevices()
    d2 = I2Cscanner()
    print d2.devices, ;
    print d2.scanned


def testGetInfoRasp():
    # detect if in linux
    with open('/proc/cpuinfo', 'r') as cpu:
        cpuinfo = cpu.read()
    cpuinfo = cpuinfo.replace('\t', '').splitlines()
    for info in cpuinfo:
        if info.find('BCM2708') > 0:
            print 'encontrado Pi 1'
        if info.find('BCM2709') > 0:
            print 'encontrado Pi 2'
    # implementar sensor virtual si no se encontro board


if __name__ == "__main__":
    try:
        test()
        # testGetInfoRasp()
    except KeyboardInterrupt:
        print 'saliendo'
