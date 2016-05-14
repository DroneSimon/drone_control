#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import mock

import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    import DroneFramework.drivers.driverUltrasonido
    from DroneFramework.drivers.driverUltrasonido import DriverUltrasonido
    direcionDriver=DroneFramework.drivers.driverUltrasonido.DriverUltrasonido
    raspberry = True
else:
    import DroneFramework.drivers.virtual.driverUltrasonidoVirtual
    from DroneFramework.drivers.virtual.driverUltrasonidoVirtual import DriverUltrasonidoVirtual as DriverUltrasonido
    direcionDriver=DroneFramework.drivers.virtual.driverUltrasonidoVirtual.DriverUltrasonidoVirtual


# Esta clase testeara los metodos de la clase DriverUltrasonido del paquete drivers
class UltrasonidoSensorTest(unittest.TestCase):

    def test_getData(self):
        # instantiate our service
        refSensorUltrasonido= DriverUltrasonido()
        # llamada al metodo get_data
        print "DriverUltrasonido.getData= ",refSensorUltrasonido.getData()
        self.data = refSensorUltrasonido.getData()
        self.assertTrue(self.data is not None, 'No se reciben datos del giroscopio')
        altura = self.data['altura']
        self.assertTrue(altura >=0 and altura <= 4000, 'no esta en rango la altura: ' + str(altura))
        print "DriverUltrasonido.getData() Testeado"

    @mock.patch.object(direcionDriver , 'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorUltrasonido= DriverUltrasonido()
        # llamada al metodo get_data usado por force read
        print "DriverUltrasonido.forceRead= ",    refSensorUltrasonido.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverUltrasonido.forceRead() Testeado"
