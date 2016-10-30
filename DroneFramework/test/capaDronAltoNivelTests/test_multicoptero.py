#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import DroneFramework.capaDronAltoNivel.dronMulticoptero as dron
import DroneFramework.capaDronBajoNivel.controladorDronMulticoptero as controladorMulticoptero
import random
import time

# Esta clase testeara los metodos de la clase ControladorDronMulticoptero del paquete capaDronBajoNivel
class MulticopetroTest(unittest.TestCase):




    def setUp(self):

        self.controladorMulticoptero = controladorMulticoptero.ControladorDronMulticoptero()
        print "Iniciando pruebas DronMulticoptero "
        self.dronATestear = dron.DronMulticoptero(self.controladorMulticoptero)

    def tearDown(self):
        print "Finalizando pruebas de ControladorDronMulticoptero"
        del self.dronATestear

    def ponerDronPosicionPruebas(self, altura=10):
        #altura=10 # la distancia en que está medida?jorge
        velocidad= 40 # es la máxima velocidad jorge

        if(self.dronATestear.estaEncendido()<>True) :
           self.dronATestear.encender()

        self.dronATestear.subir(altura,velocidad)
        self.dronATestear.mantenerCoordenadas()


    # cabeceo - elevacion de la cabeza: sube/baja a los "grados" indicados por ENCIMA del eje X
    # a la velocidad(0-50) indicada
    def test_aterrizar_General(self):
        self.ponerDronPosicionPruebas()
        yInicial=self.dronATestear.posicionActual()['y']

        self.dronATestear.aterrizar()
        yFinal=self.dronATestear.posicionActual()['y']

        self.assertNotEqual(yInicial, yFinal,1)
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(yFinal,0,1)

    def test_aterrizar2(self):
        self.ponerDronPosicionPruebas()
        yInicial=self.dronATestear.posicionActual()['y']

        self.dronATestear.aterrizar2()
        yFinal=self.dronATestear.posicionActual()['y']

        # testea que la inicial y final no sean las mismaposición
        self.assertNotEqual(yInicial, yFinal,1)
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(yFinal,0,1) #testea que estpe en el piso.


