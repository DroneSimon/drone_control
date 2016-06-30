#!/usr/bin/env python
# -*- coding: utf-8 -*-
_autora_='I.C.C.'

from datetime import *
import unittest
import mock
import DroneFramework.capaDronBajoNivel.controladorDronMulticoptero as controladorDron
from DroneFramework.hal.actuadorOpenPilot import ActuadorOpenPilot
# Esta clase testeará los métodos de la clase ControladorDronMulticoptero del módulo dronBajoNivel

class ControladorDronMulticopteroTest(unittest.TestCase):

    def setUp(self):
         self.controladorDron = controladorDron.ControladorDronMulticoptero()

    def tearDown(self):
        self.controladorDron.dispose()
        self.controladorDron = None

    def test_getData_NoNone(self):

        self.assertIsNotNone(self.controladorDron)

    def test_encender(self):
         op=mock.create_autoespec(ActuadorOpenPilot)
         controladorDron.encender()
         # con esto testeo que se ejecutó el openPilo.encender(), una sola vez
         self.assertEquals(op.encender.call_count,1)
         print 'metodo encender testeado: se llamó una vez a openPilot.encender()'

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ControladorDronMulticopteroTest('test_encender'))
        suite.addTest(ControladorDronMulticopteroTest('test_getData_NoNone'))
        return suite


    def test_setData(self):

        dataUltrasonido = self.dataUltrasonido
        new_data = {'altura': 50}
        dataUltrasonido.setData(new_data)
        self.assertEquals(dataUltrasonido.getData(), new_data)

    def test_getAge(self):

        self.assertIsNotNone(self.dataUltrasonido.getData())

    def test_setAge(self):

        dataUltrasonido = self.dataUltrasonido
        new_age = datetime.today()
        dataUltrasonido.setAge(new_age)
        self.assertEquals(dataUltrasonido.getAge(), new_age)