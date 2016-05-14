#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import mock

import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    import DroneFramework.drivers.driverGPS
    from DroneFramework.drivers.driverGPS import DriverGPS
    direccionDriver=DroneFramework.drivers.driverGPS.DriverGPS
    raspberry = True
else:
    import DroneFramework.drivers.virtual.driverGPSvirtual
    from DroneFramework.drivers.virtual.driverGPSvirtual import DriverGPSvirtual as DriverGPS
    direccionDriver=DroneFramework.drivers.virtual.driverGPSvirtual.DriverGPSvirtual



# Esta clase testeará los metodos de la clase DriverGPS del paquete drivers
# Se enmascará el comportamiento de serial de la raspberry
class GPSSensorTest(unittest.TestCase):

    #notar el orden de los parámetros: el módulo exterior primero, luego el más interno y así sucesivamente
    #@mock.patch('DroneFramework.drivers.driverGPS.serial')
    #@mock.patch.object(DroneFramework.drivers.driverGPS,'ser', autospect=True)
    def test_getData(self):
        # instantiate our service
        refSensorGPS= DriverGPS()
        '''   # set up the mock
        mock_ser.readline.return_value = "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
        # llamada al metodo get data
        print "DriverGPS.getData= ",refSensorGPS.getData()
        self.assertTrue(mock_ser.readline.called, "Error no se ejecutó el Serial.readline")
        print "DriverGPS.getData() Testeado"
        '''
        print "DriverGPS.getData= ",refSensorGPS.getData()
        self.data = refSensorGPS.getData()
        self.assertTrue(self.data is not None, 'No se reciben datos del giroscopio')
        self.latitud = self.data['latitud']
        self.longitud= self.data['longitud']
        self.altitud= self.data['altitud']
        self.assertTrue(self.latitud >= -180.0 and self.latitud <= 180.0, 'no esta en rango latitud: ' + str(self.latitud))
        self.assertTrue(self.longitud >= -180 and self.longitud <= 180, 'no esta en rango longitud: ' + str(self.longitud))
        self.assertTrue(self.altitud >= -10000 and self.altitud <= 10000, 'no esta en rango altitud: ' + str(self.altitud))
        print "DriverGPS.getData() Testeado"


    @mock.patch.object(direccionDriver, 'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorGPS= DriverGPS()
        # llamada al metodo get_data
        print "DriverGPS.forceRead= ",refSensorGPS.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverGPS.forceRead() Testeado"
