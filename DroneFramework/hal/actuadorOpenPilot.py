# -*- coding: utf-8 -*-
_autor_ = "Jorge Encinas"

from time import sleep

import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    import serial
    raspberry = True
else:
    import DroneFramework.drivers.serial_paraCorrerEnPC as serial

class ActuadorOpenPilot:
	"""control PWM para 6 canales en Modo 2"""
	def __init__( self ):
		self.ser = serial.Serial( port='/dev/ttyUSB0', baudrate = 9600 )
		self.throttle = 0
		self.roll = 50
		self.pitch = 50
		self.yaw = 50
		self.flightMode = 0
		self.accessory0 = 0

	def writeSerial(self, cad):
		self.ser.write(cad)

	def reiniciar( self ):
		print "no implementado reinicar no sería lo mismo que reset?"
	""" uso para except KeyboardInterrupt o similares"""
	def interrumpir( self ):
		print "no implementado interrumpir"

	def encender(self):
			self.setRoll(50)
			self.setPith(50)
			self.setThrottle(0)
			self.setYaw(100) # configurado en openpilot
			sleep(2)
			print "armado"

	def setOnOf(self, valor):
		if(valor == 1):
			self.setRoll(50)
			self.setPith(50)
			self.setThrottle(0)
			self.setYaw(100) # configurado en openpilot
			sleep(2)
			print "armado"
		elif(valor == 0):
			self.setRoll(50)
			self.setPith(50)
			self.setThrottle(0)
			self.setYaw(0) # configurado en openpilot
			sleep(2)
			print "apagado"

	def setRoll(self, vel):
		self.roll = vel
		self.writeSerial( 'r' + str(vel))

	def setPith(self, vel):
		self.pith = vel
		self.writeSerial( 'p' + str(vel))

	def setThrottle(self, vel):
		self.throttle = vel
		self.writeSerial( 't' + str(vel))

	def setYaw(self, vel):
		self.yaw = vel
		self.writeSerial( 'y' + str(vel))

	def setModoVuelo(self, modo):
		self.flightMode = modo
		self.writeSerial( 'f' + str(modo))

	def setAux2(self, vel):
		self.accessory0 = vel
		self.writeSerial( 'a' + str(vel))

	def getRoll(self):
		return self.roll

	def getPitch(self):
		return self.pitch

	def getThrottle(self):
		return self.throttle

	def getYaw(self):
		return self.yaw

	def getModoVuelo(self):
		return self.flightMode

	def getAux2(self):
		return self.accessory0


	def resetearValores(self):
		self.throttle = 0
		self.roll = 50
		self.pitch = 50
		self.yaw = 50
		self.flightMode = 0
		self.accessory0 = 0