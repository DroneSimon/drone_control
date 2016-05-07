from mock import MagicMock


class GpsMock (object):

    def readline(self):

        archivo = open("gpsDataCaptured.serial","r")
        #archivo = open("/drone_control/DroneFramework/mocks/gpsDataCaptured.serial","r")
        linea1 = archivo.readline()
        sensorGPS = MagicMock(return_value=linea1)
        print sensorGPS.return_value
        return linea1

