#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock
from DroneFramework.drivers.driverMagnetometro import DriverMagnetometro
import DroneFramework.drivers.driverMagnetometro
# Esta clase testeara los metodos de la clase DriverMagnetómetro del paquete drivers
# Se enmascará el comportamiento el objeto bus de móduo driverMagnetometro
# que es una instancia de smbus.SMBus.(0), que implementa la raspberry
class MagnetometroSensorTest(unittest.TestCase):

    @mock.patch.object(DroneFramework.drivers.driverMagnetometro,'bus', autospect=True)
    def test_getData(self, mock_bus):
        # instantiate our service
        refSensorMagentometro= DriverMagnetometro()
        # set up the mock
        mock_bus.read_byte_data.return_value = "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
        # llamada al metodo get data
        print "DriverMagnetometro.getData= ",refSensorMagentometro.getData()
        self.assertTrue(mock_bus.read_byte_data.called, "Error no se ejecuto el SMBus.read_byte_data")
        self.assertTrue(mock_bus.write_byte_data.called, "Error no se ejecuto el SMBus.write_byte_data")
        print "DriverMagnetometro.getData() Testeado"

    @mock.patch.object(DroneFramework.drivers.driverMagnetometro.DriverMagnetometro,'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorMagnetometro= DriverMagnetometro()
        # llamada al metodo get_data usado por force read
        print "DriverMagnetometro.forceRead= ",    refSensorMagnetometro.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverMagnetometro.forceRead() Testeado"