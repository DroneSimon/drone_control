#!/usr/bin/env python
# -*- coding: utf-8 -*-
__autora__='I.C.C.'

import unittest
import DroneFramework.capaDronBajoNivel.controladorDronMulticoptero as controladorDron
import random
import time

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

    # giro lateral de costado a la DERECHA: x giroscopio positivo
    # deja el dron en "grados" a la DERECJA EJE X a la "velocidad" indicada
    # =======================================================================
    def test_roll_derecha_casos(self):
        velocidad=random.randrange(1, 50, 1) # del 1-50 de 1 en 1. 1-50 es la velocidad que imprime ol Open Pilot
        grados= random.randrange(1, 360, 1) # del 1-360 de 1 en 1. 1-360 es el grados a la derecha del eje que queremos estar
        xInicial=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']

        # si velocidad es 0, no debería moverse
        self.controladorDronATestear.roll_derecha(grados,0)
        xFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']
        self.assertAlmostEqual(xInicial,xFinal ,1) # el 1 indica que puede variar desde el primer decimal

        # si velocidad >0, ponemos x a 80 grados
        self.test_roll_derecha(80,velocidad)

        # si velocidad >0, ponemos x a 0 grados, notar que ahora está en 80 e irá de 80 a 0, ed a a izquierda
        self.test_roll_derecha(0,velocidad) # notar que es 0 grados a la DERECHA EJE X

        # si velocidad >0, ponemos x a 20 grados, notar que ahora está en 0 e irá de 0 a 20, ed a la derecha
        self.test_roll_derecha(20,velocidad) # notar que es 0 grados a la DERECHA EJE X

    def test_roll_derecha(self, grados=45, velocidad=30):
        print "Testeando roll_derecha   grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.roll_derecha(grados,velocidad)
        xFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados,xFinal ,1) # el 1 indica que puede variar desde el primer decimal

    # giro lateral de costado a la IZQUIERDA: x giroscopio positivo
    # deja el dron en "grados" a la IZQUIERDA EJE X a la "velocidad" indicada
    # =======================================================================
    def test_roll_izquierda_casos(self):
        velocidad=random.randrange(1, 50, 1) # del 1-50 de 1 en 1. 1-50 es la velocidad que imprime ol Open Pilot
        grados= random.randrange(1, 360, 1) # del 1-360 de 1 en 1. 1-360 es el grados a la izquierda del eje que queremos estar
        xInicial=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']

        # si velocidad es 0, no debería moverse
        self.controladorDronATestear.roll_izquierda(grados,0)
        xFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']
        self.assertAlmostEqual(xInicial,xFinal ,1) # el 1 indica que puede variar desde el primer decimal

        # si velocidad >0, ponemos x a -80 grados
        self.test_roll_izquierda(80,velocidad)

        # si velocidad >0, ponemos x a 0 grados, notar que ahora está en -80 e irá de -80 a 0, ed a a derecha
        self.test_roll_izquierda(0,velocidad) # notar que es 0 grados a la izquierda EJE X

        # si velocidad >0, ponemos x a -20 grados, notar que ahora está en 0 e irá de 0 a -20, ed a la izquierda
        self.test_roll_izquierda(20,velocidad) # notar que es 0 grados a la izquierda EJE X

    def test_roll_izquierda(self, grados=45, velocidad=30):
        print "Testeando roll_izquierda   grados=",grados," velocidad=",velocidad
        self.controladorDronATestear.roll_izquierda(grados,velocidad)
        xFinal=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()['x']
        # el 1 de abajo indica que puede variar desde el primer decimal
        self.assertAlmostEqual(grados,xFinal ,1) # el 1 indica que puede variar desde el primer decimal

    # devuelve los angulos x, y z en un diccionario
    def test_getAnguloCabeza(self):
        data1=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()
        self.assertTrue(isinstance(data1['x'], float)  & isinstance(data1['y'],float) & isinstance(data1['z'],float) & isinstance(data1['inclinacion_x'],float) & isinstance(data1['inclinacion_y'],float))
        data2=self.controladorDronATestear.sensorGiroscopio.getLastInfo().getData()

        self.assertAlmostEqual(data1, data2 ,1) # el 1 indica que puede variar desde el primer decimal

    # devuelve x y z (longitud, latitud y altura al suelo en cm) como una tupla
    def test_getCoordenadas(self):
        xyz1=self.controladorDronATestear.sensorGPS.getCoordenadas()
        self.assertIsNotNone(self.controladorDronATestear.sensorGPS.getLastInfo().getData())
        self.assertTrue((xyz1['latitud']>=0.0 or xyz1['latitud']<0.0) and (xyz1['longitud'] >=0.0 or  xyz1['longitud'] <0.0) and (xyz1['altitud']>=0.0 or  xyz1['altitud']<0.0 ) )
        xyz1=self.controladorDronATestear.getCoordenadas()
        self.assertIsNotNone(self.controladorDronATestear.sensorGPS.getLastInfo().getData())
        self.assertTrue((xyz1['x']>=0.0 or xyz1['x']<0.0) and (xyz1['y'] >=0.0 or  xyz1['y'] <0.0) and (xyz1['z']>=0.0 or  xyz1['z']<0.0 ) )

        xyz2=self.controladorDronATestear.getCoordenadas()
        self.assertAlmostEqual(xyz1, xyz2 ,1) # el 1 indica que puede variar desde el primer decimal

    # avanza el dron en direccion a al acabeza
    # se asumió para la prueba que  se mueve en el eje x
    def test_irAdelante(self):
        xyz1=self.controladorDronATestear.getCoordenadas()
        self.controladorDronATestear.irAtras(30)
        time.sleep(.900)
        xyz2=self.controladorDronATestear.getCoordenadas()
        if (xyz1['x']>0):
            self.assertTrue(xyz2['x']>xyz1['x'])
        else:
             self.assertTrue(xyz2['x']<xyz1['x'])

    # avanza el dron en direccion contraria a la cabeza
    # se asumió para la prueba que  se mueve en el eje x
    def test_irAtras(self):
        xyz1=self.controladorDronATestear.getCoordenadas()
        self.controladorDronATestear.irAtras(30)
        time.sleep(.900)
        xyz2=self.controladorDronATestear.getCoordenadas()
        if (xyz1['x']>0):
            self.assertTrue(xyz2['x']<xyz1['x'])
        else:
             self.assertTrue(xyz2['x']>xyz1['x'])


    # avanza el dron hacia la derecha de su cabeza
    # se asumió para la prueba que  se mueve en el eje y
    def test_irDerecha(self):
        xyz1=self.controladorDronATestear.getCoordenadas()
        self.controladorDronATestear.irAtras(30)
        time.sleep(.900)
        xyz2=self.controladorDronATestear.getCoordenadas()
        if (xyz1['y']>0):
            self.assertTrue(xyz2['y']>xyz1['y'])
        else:
             self.assertTrue(xyz2['y']<xyz1['y'])

    # avanza el dron hacia la izquierda de su cabeza
    # se asumió para la prueba que  se mueve en el eje y
    def test_irIzquierdad(self):
        xyz1=self.controladorDronATestear.getCoordenadas()
        self.controladorDronATestear.irAtras(30)
        time.sleep(.900)
        xyz2=self.controladorDronATestear.getCoordenadas()
        if (xyz1['y']<0):
            self.assertTrue(xyz2['y']<xyz1['y'])
        else:
             self.assertTrue(xyz2['y']>xyz1['y'])

    #Nivela dron se asume que queda nivelado si "x" y "y"  están muuy cerca de cero
    def test_nivelarDron(self):
        self.controladorDronATestear.nivelarDron()
        xyz=self.controladorDronATestear.getCoordenadas()
        self.assertAlmostEquals(xyz['x'],0,1) # uno es el error esperado en este caso desde el 1er decimal
        self.assertAlmostEquals(xyz['y'],0,1)

    # estabilizado - acrobatico y tiene 6 modos mas
    def test_setModo_getModo(self):
        self.controladorDronATestear.setModo(0)
        self.assertEquals(self.controladorDronATestear.getModo(),0,1) # uno es el error esperado en este caso desde el 1er decimal

        self.controladorDronATestear.setModo(1)
        self.assertEquals(self.controladorDronATestear.getModo(),1,1) # uno es el error esperado en este caso desde el 1er decimal

    #nivela dron para quedarse en el mismo lugar
    def test_mantenerCoordenadas(self):
        self.controladorDronATestear.mantenerCoordenadas()
        xyz1=self.controladorDronATestear.getCoordenadas()
        time.sleep(.900)
        xyz2=self.controladorDronATestear.getCoordenadas()
        self.assertAlmostEquals(xyz1['x'],xyz2['x'],1) # uno es el error esperado en este caso desde el 1er decimal
        self.assertAlmostEquals(xyz1['y'],xyz2['y'],1)
        self.assertAlmostEquals(xyz1['z'],xyz2['z'],1)

    # devuelve los valores de modos de vuelo en un diccionario:{'estabilizado', 'acrobatico'}
    def test_getModosDeOperacion(self):
        diccionario=self.controladorDronATestear.getModosDeOperacion()
        self.assertTrue(isinstance(diccionario,dict))
