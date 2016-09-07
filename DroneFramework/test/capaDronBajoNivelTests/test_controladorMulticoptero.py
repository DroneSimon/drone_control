#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import DroneFramework.capaDronBajoNivel.controladorDronMulticoptero as controladorDron
import random

# Esta clase testeara los metodos de la clase ControladorDronMulticoptero del paquete capaDronBajoNivel
class ControladorMulticopetroTest(unittest.TestCase):

    def setUp(self):
        print "Iniciando pruebas ControladorDronMulticoptero "
        self.controladorDronATestear = controladorDron.ControladorDronMulticoptero()
    def tearDown(self):
        print "Finalizando pruebas de ControladorDronMulticoptero"
        del self.controladorDronATestear

    # cabeceo - elevacion de la cabeza: sube/baja a los "grados" indicados por ENCIMA del eje X
    # a la velocidad(0-50) indicada
    def test_pitch_arribaGeneral(self):
        # cabeza 1er cuadrante
        grados=30
        self.test_pitch_arriba(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        # cabeza 2do cuadrante
        grados=120
        self.test_pitch_arriba(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        #cabeza 3er cuadrante
        grados=210
        self.test_pitch_arriba(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        #cabeza 4to cuadrante
        grados=300
        self.test_pitch_arriba(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)



    # No debería moverse
    def test_pitch_arriba_conVelocidadCero(self):
        grados= random.randrange(0, 360, 1) # de angulo 0-360 de 1 en 1
        velocidad=0
        yInicial= self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        print "Testeando con velocidadCero grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_arriba(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        self.assertEqual(yInicial, yFinal)

    #Debería dejar la cabeza muuuy cerca de cero grados
    def test_pitch_arriba_aCeroGrados(self):
        grados=0
        velocidad=random.randrange(1, 50, 1) # del 0-50 de 1 en 1. 0-50 es la velocidad que imprime ol Open Pilot

        print "Testeando pitch  aCeroGrados  grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_arriba(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(0, yFinal,1)

    def test_pitch_arriba(self,grados=80):
        velocidad=random.randrange(1, 50, 1) # del 0-50 de 1 en 1. 0-50 es la velocidad que imprime ol Open Pilot

        print "Testeando pitch_arriba   grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_arriba(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados,yFinal ,1)

    # cabeceo - elevacion de la cabeza: sube/baja a los "grados" indicados por DEBAJO del eje X
    # a la velocidad(0-50) indicada
    def test_pitch_abajoGeneral(self):
        # cabeza 1er cuadrante
        grados=30
        self.test_pitch_abajo(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        # cabeza 2do cuadrante
        grados=120
        self.test_pitch_abajo(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        #cabeza 3er cuadrante
        grados=210
        self.test_pitch_abajo(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

        #cabeza 4to cuadrante
        grados=300
        self.test_pitch_abajo(grados)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados, yFinal,1)

    # No debería moverse
    def test_pitch_abajo_conVelocidadCero(self):
        grados= random.randrange(0, 360, 1) # de angulo 0-360 de 1 en 1
        velocidad=0
        yInicial= self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        print "Testeando con velocidadCero grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_abajo(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        self.assertEqual(yInicial, yFinal)

    #Debería dejar la cabeza muuuy cerca de cero grados
    def test_pitch_abajo_aCeroGrados(self):
        grados=0
        velocidad=random.randrange(1, 50, 1) # del 0-50 de 1 en 1. 0-50 es la velocidad que imprime ol Open Pilot

        print "Testeando pitch  aCeroGrados  grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_abajo(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(0, yFinal,1)

    def test_pitch_abajo(self,grados=80):
        velocidad=random.randrange(1, 50, 1) # del 0-50 de 1 en 1. 0-50 es la velocidad que imprime ol Open Pilot

        print "Testeando pitch_abajo   grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.pitch_abajo(grados,velocidad)
        yFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['y']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados,yFinal ,1)





