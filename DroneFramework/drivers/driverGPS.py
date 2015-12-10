import time
import serial
import re, os
import pynmea2

ser = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 4800 ,
    timeout = 1
)

try:
	while 1 :
		time.sleep( 0.1 )
		linea = str( ser.readline() )
		if re.match( "\$GPGGA" , linea ):
			partes_linea = pynmea2.parse( linea )
			if partes_linea.latitude:
				os.system( "clear" )
				print "Latitude:\t %s"%partes_linea.latitude
				print "Longitude:\t %s"%partes_linea.longitude
				print "Altitude:\t %s"%partes_linea.altitude
				print "\n==========================================\n"
except KeyboardInterrupt:
	ser.flush()
	ser.close()


#modified by Diego Garcia
from driver import Driver
class DriverGPS(Driver):

	def getData(self):

		while True :
			time.sleep( 0.1 )
			linea = str( ser.readline() )
			if re.match( "\$GPGGA" , linea ):
				partes_linea = pynmea2.parse( linea )
				if partes_linea.latitude:
					data = dict()
					data['latitud'] = partes_linea.latitude
					data['longitud'] = partes_linea.longitude
					data['altitud'] = partes_linea.altitude
					return data

	def getStatus(self):
		# tiene los datos del sensor
        # ok, no_ok, excepcion,
		raise NotImplementedError( "Should have implemented this" )

	def forceRead(self):
		# fuerza a hacer una nueva lectura al sensor
		return self.getData()

	def reset(self):
		# inicializa datos sensor
		raise NotImplementedError( "Should have implemented this" )