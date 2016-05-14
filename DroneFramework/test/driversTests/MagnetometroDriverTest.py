#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import mock

import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    import DroneFramework.drivers.driverMagnetometro
    from DroneFramework.drivers.driverMagnetometro import DriverMagnetometro
    direcionDriver=DroneFramework.drivers.driverMagnetometro.DriverMagnetometro
    raspberry = True
else:
    import DroneFramework.drivers.virtual.driverMagnetometroVirtual
    from DroneFramework.drivers.virtual.driverMagnetometroVirtual import DriverMagnetometroVirtual as DriverMagnetometro
    direcionDriver=DroneFramework.drivers.virtual.driverMagnetometroVirtual.DriverMagnetometroVirtual





# Esta clase testeara los metodos de la clase DriverMagnetómetro del paquete drivers
# Se enmascará el comportamiento el objeto bus de móduo driverMagnetometro
# que es una instancia de smbus.SMBus.(0), que implementa la raspberry
class MagnetometroSensorTest(unittest.TestCase):

    def test_getData(self):
        # instantiate our service
        refSensorMagentometro= DriverMagnetometro()
        print "DriverMagnetometro.getData= ",refSensorMagentometro.getData()
        self.data=refSensorMagentometro.getData()
        self.assertTrue(self.data is not None, 'No se reciben datos del giroscopio')
        # llamada al metodo get data
        angulo = self.data['angulo']
        self.assertTrue(angulo>= -180.0 and angulo <= 180.0, 'no esta en rango angulo= -180 y 180 : ' + str(angulo))
        print "DriverMagnetometro.getData() Testeado"

    @mock.patch.object(direcionDriver,'getData', autospect=True)
    def test_forceRead(self,mock_getData):
        # instantiate our service
        refSensorMagnetometro= DriverMagnetometro()
        # llamada al metodo get_data usado por force read
        print "DriverMagnetometro.forceRead= ",    refSensorMagnetometro.forceRead()
        self.assertTrue(mock_getData.called, "Error no se ejecuto el getData()")
        print "DriverMagnetometro.forceRead() Testeado"
