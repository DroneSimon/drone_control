import unittest

import cpuinfo

raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    from DroneFramework.drivers.driverGiroscopio import DriverGiroscopio

    raspberry = True
else:
    from DroneFramework.drivers.virtual.driverGiroscopioVirtual import DriverGiroscopioVirtual as DriverGiroscopio


class TestDriverMethods(unittest.TestCase):
    def setUp(self):
        self.giroscopio = DriverGiroscopio()

    # def exitTestFunc(self):
    #     with self.assertRaises(SystemExit):
    #         if not raspberry:
    #             self.giroscopio.stop()
    #             print "Giroscope Thread stop"
    #         exit(0)
    def tearDown(self):
        if not raspberry:
            self.giroscopio.stop()
            print "Giroscope Thread stop"


class testDriverGetData(TestDriverMethods):
    def runTest(self):
        self.data = self.giroscopio.getData()
        self.assertTrue(self.data is not None, 'Sin recibir datos del sensor')
        self.x = self.data['inclinacion_x']
        self.y = self.data['inclinacion_y']
        self.assertTrue(self.x >= -180.0 and self.x <= 180.0, 'no esta en rango x: ' + str(self.x))
        self.assertTrue(self.y >= -180 and self.y <= 180, 'no esta en rango y: ' + str(self.y))


class testDriverGetStatus(TestDriverMethods):
    def runTest(self):
        self.status = self.giroscopio.getStatus()
        self.assertTrue(self.status is not None, 'no se puede obtener el estado')
        self.assertTrue(self.status is 'ok'
                        or self.status is 'no ok'
                        # or self.status is EXCEPTION
                        , ' no se puede obtener el estado')


class testDriverForceRead(TestDriverMethods):
    # dato anterio es igual al actual,
    # sensor status no ok o no dejo de responder y reiniciar
    def runTest(self):
        self.data = self.giroscopio.getData()
        self.assertTrue(self.data is not None, 'Sin recibir datos del sensor')
        self.x = self.data['inclinacion_x']
        self.y = self.data['inclinacion_y']
        self.assertTrue(self.x >= -180.0 and self.x <= 180.0, 'no esta en rango x: ' + str(self.x))
        self.assertTrue(self.y >= -180 and self.y <= 180, 'no esta en rango y: ' + str(self.y))


class testDriverReset(TestDriverMethods):
    # reiniciar el sensor
    def runTest(self):
        raise NotImplementedError("unit test no implementado")


if __name__ == '__main__':
    unittest.main()
