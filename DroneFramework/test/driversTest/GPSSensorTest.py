#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock
from DroneFramework.drivers.driverGPS import DriverGPS
import DroneFramework.drivers.driverGPS
# Esta clase testeara la clase los metodos de la clase DriverGPS del paquete drivers
# Se enmascará el comportamiento de serial de la raspberry
class GPSSensorTest(unittest.TestCase):

    #notar el orden de los parámetros: el módulo exterior primero, luego el más interno y así sucesivamente
    @mock.patch('DroneFramework.drivers.driverGPS.serial')
    @mock.patch.object(DroneFramework.drivers.driverGPS,'ser', autospect=True)
    def test_getData(self, mock_ser,mock_serial):
        # instantiate our service
        refSensorGPS= DriverGPS()
        # set up the mock
        mock_ser.readline.return_value = "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
        # llamada al metodo get data
        print "DriverGPS.getData= ",refSensorGPS.getData()
        self.assertTrue(mock_ser.readline.called, "Error no se ejecuto el Serial.readline")
        print "DriverGPS.getData() Testeado"

    @mock.patch.object(DroneFramework.drivers.driverGPS.DriverGPS,'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorGPS= DriverGPS()
        print "se inicializo el modulo serial usado por GPS"
        # set up the mock

        # llamada al metodo get data
        print "DriverGPS.forceRead= ",refSensorGPS.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverGPS.forceRead() Testeado"
