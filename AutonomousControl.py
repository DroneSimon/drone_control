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

#from DroneFramework.test.ejerciciosConMocks.moduloDeLlamadaATests import correrEjerciciosDeTestConMocks
#from DroneFramework.test.driversTests.correrTestDeDrivers import correrTestDeDrivers
from DroneFramework.capaDronBajoNivel.controladorDronMulticoptero import ControladorDronMulticoptero

from DroneFramework.test.capaDronBajoNivelTests.test_dronDronMulticopteroCapa3 import ControladorDronMulticopteroTest
def main():
    #correrEjerciciosDeTestConMocks()
    #correrTestDeDrivers()
    #dron= ControladorDronMulticoptero()
    #dron.encender()

    testSuiteControladorDron=ControladorDronMulticopteroTest('suite')
    correr=testSuiteControladorDron()
    #correr()




if __name__ == '__main__':
	main()

