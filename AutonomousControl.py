# -*- coding: utf-8 -*-
import os
#os.chdir("D:\\tallerDrones\\gitFM\drone_control\\DroneFramework\\mocks")
os.path.join(os.getcwd(), 'DroneFramework', 'mocks')

#import DroneFramework.drivers.driverGPS as GPS_driver

import Reconocedor_Fuego_Humo as fire_detector
from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero as drone

def anomalyDetect(img):
    detected = False;
    return fire_detector.detectar_fuego_humo(img)

def anomalyDetectedOK():
    the_drone = drone.ControladorDronMulticoptero()
    the_drone.encender()
    the_drone.up(10, 0)
    the_drone.yaw(360, 10)
    the_drone.down(10,1)
    the_drone.apagar()
#1.
#from DroneFramework.test.ejerciciosConMocks.moduloDeLlamadaATests import correrEjerciciosDeTestConMocks
#2.
#from DroneFramework.test.driversTests.correrTestDeDrivers import correrTestDeDrivers
#3.
from DroneFramework.test.capaDronBajoNivelTests.correrTestCtrlDronMulticoptero import CorrerTestCtrlDronMulticoptero
#4.
#from DroneFramework.test.capaDronAltoNivelTests.correrTestDronMulticoptero import CorrerTestDronMulticoptero


#from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero

#from DroneFramework.capaDronAltoNivel.dronMulticoptero import DronMulticoptero


def main():
    #1.
    #correrEjerciciosDeTestConMocks()
    #2.
    #correrTestDeDrivers()
    #3.
    correrTestCtrlMulticoptero= CorrerTestCtrlDronMulticoptero()
    correrTestCtrlMulticoptero.correrTest()

    #4.
    #correrTestMulticoptero= CorrerTestDronMulticoptero()
    #correrTestMulticoptero.correrTest()


    #dron= DronMulticoptero(controladorMulticoptero)
    #dron.encender()



if __name__ == '__main__':
	main()

