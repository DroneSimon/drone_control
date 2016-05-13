#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from DroneFramework.drivers.driverUltrasonido import DriverUltrasonido
import DroneFramework.drivers.driverUltrasonido

import cpuinfo

raspberry = False
info = cpuinfo.get_cpu_info()

if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    from DroneFramework.drivers.driverUtrasonido import DriverUltrasonido

    raspberry = True
else:
    from DroneFramework.drivers.virtual.driverUltrasonidoVirtual import DriverUltrasonidoVirtual as DriverUltrasonido

import DroneFramework.drivers.RPi.GPIO as GPIO
# Esta clase testeara los metodos de la clase DriverUltrasonido del paquete drivers
# Se enmascarará el comportamiento el objeto RPi.GPIO de móduo driverUltrasonido
class UltrasonidoSensorTest(unittest.TestCase):

    def test_getData(self):
        # instantiate our service
        refSensorUltrasonido= DriverUltrasonido()
        # llamada al metodo get_data
        print "DriverGiroscopio.getData= ",refSensorUltrasonido.getData()
        print "DriverGiroscopio.getData() Testeado"
    if raspberry:
        direcionDriver=DroneFramework.drivers.driverUltrasonido.DriverUltrasonido
    else:
        direcionDriver=DroneFramework.drivers.virtual.driverUltrasonidoVirtual.DriverUltrasonidoVirtual
    @mock.patch.object(direcionDriver , 'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorUltrasonido= DriverUltrasonido()
        # llamada al metodo get_data usado por force read
        print "DriverUltrasonido.forceRead= ",    refSensorUltrasonido.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverUltrasonido.forceRead() Testeado"
