#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import mock

import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    import DroneFramework.drivers.driverGiroscopio
    from DroneFramework.drivers.driverGiroscopio import DriverGiroscopio
    direcionDriver=DroneFramework.drivers.driverGiroscopio.DriverGiroscopio
    raspberry = True
else:
    import DroneFramework.drivers.virtual.driverGiroscopioVirtual
    from DroneFramework.drivers.virtual.driverGiroscopioVirtual import DriverGiroscopioVirtual as DriverGiroscopio
    direcionDriver=DroneFramework.drivers.virtual.driverGiroscopioVirtual.DriverGiroscopioVirtual



# Esta clase testeara los metodos de la clase DriverGiroscopio del paquete drivers
# Se enmascará el comportamiento el objeto bus de móduo driverGiroscopio
# que es una instancia de smbus.SMBus.(0), que implementa la raspberry
class GiroscopioSensorTest(unittest.TestCase):

   #@mock.patch.object(DroneFramework.drivers.driverGiroscopio,'bus', autospect=True)
    def test_getData(self):
        # instantiate our service
        refSensorGiroscopio= DriverGiroscopio()
        # set up the mock
        #mock_bus.read_byte_data.return_value = "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
        # llamada al metodo get data
        print "DriverGiroscopio.getData= ",refSensorGiroscopio.getData()
        #self.assertTrue(mock_bus.read_byte_data.called, "Error no se ejecuto el SMBus.read_byte_data")
        #self.assertTrue(mock_bus.write_byte_data.called, "Error no se ejecuto el SMBus.write_byte_data")
        #print "DriverGiroscopio.getData() Testeado"


        self.data = refSensorGiroscopio.getData()
        self.assertTrue(self.data is not None, 'No se reciben datos del giroscopio')
        self.x = self.data['inclinacion_x']
        self.y = self.data['inclinacion_y']
        self.assertTrue(self.x >= -180.0 and self.x <= 180.0, 'no esta en rango x: ' + str(self.x))
        self.assertTrue(self.y >= -180 and self.y <= 180, 'no esta en rango y: ' + str(self.y))
        print "DriverGiroscopio.getData() Testeado"

    @mock.patch.object(direcionDriver,'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorGiroscopio= DriverGiroscopio()
        # llamada al metodo get_data usado por force read
        print "DriverGiroscopio.forceRead= ",    refSensorGiroscopio.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverGiroscopio.forceRead() Testeado"
'''
class testDriverGetStatus(TestDriverMethods):
    def runTest(self):
        self.status = self.giroscopio.getStatus()
        self.assertTrue(self.status is not None, 'no se puede obtener el estado')
        self.assertTrue(self.status is 'ok'
                        or self.status is 'no ok'
                        # or self.status is EXCEPTION
                        , ' no se puede obtener el estado')
'''