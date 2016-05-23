__autora__='I.C.C.'


from DroneFramework.test.driversTests.GPSDriverTest import GPSSensorTest
from DroneFramework.test.driversTests.MagnetometroDriverTest import MagnetometroSensorTest
from DroneFramework.test.driversTests.GiroscopioDriverTest import GiroscopioSensorTest
from DroneFramework.test.driversTests.UltrasonidoDriverTest import UltrasonidoSensorTest

def correrTestDeDrivers():
    #driverGPS Test
    #==============
    print "\n------------------   TEST GPS   --------------------"
    testGPSDriver=GPSSensorTest('test_getData')
    testGPSDriver.test_getData()
    testGPSDriver.test_forceRead()

    #driverUltrasonido Test
    #=======================
    print "\n ------------------   TEST ULTRASONIDO   --------------------"
    testUltrasonidoDriver=UltrasonidoSensorTest('test_getData')
    testUltrasonidoDriver.test_getData()
    testUltrasonidoDriver.test_forceRead()

    #driverMagnetometro Test
    #=======================
    print "\n ------------------   TEST MAGNETOMETRO   --------------------"
    testMagnetometroDriver=MagnetometroSensorTest('test_getData')
    testMagnetometroDriver.test_getData()
    testMagnetometroDriver.test_forceRead()

    #driverGiroscopio Test
    #=======================
    print "\n------------------   TEST GIROSCOPIO   --------------------"
    testGiroscopioDriver=GiroscopioSensorTest('test_getData')
    testGiroscopioDriver.test_getData()
    testGiroscopioDriver.test_forceRead()