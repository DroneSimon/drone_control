_autor_ = "Jorge Encinas"

from time import sleep
import serial

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

	def setOnOf(self, valor):
		if(valor == 1):
			setRoll(50)
			setPith(50)
			setThrottle(0)
			setYaw(100) # configurado en openpilot
			sleep(2)
			print "armado"
		elif(valor == 0):
			setRoll(50)
			setPith(50)
			setThrottle(0)
			setYaw(0) # configurado en openpilot
			sleep(2)
			print "armado"
		
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

	def setModoVuelo(self, vel):
		self.flightMode = vel
		self.writeSerial( 'f' + str(vel))

	def setAux2(self, vel):
		self.accessory0 = vel
		self.writeSerial( 'a' + str(vel))

	def getRoll(self):
		return self.roll.valor

	def getPitch(self):
		return self.pitch.valor

	def getThrottle(self):
		return self.throttle.valor

	def getYaw(self):
		return self.yaw.valor

	def getModoVuelo(self):
		return self.flightMode.valor

	def getAux2(self):
		return self.accessory0.valor


	def resetearValores(self):
		self.throttle = 0
		self.roll = 50
		self.pitch = 50
		self.yaw = 50
		self.flightMode = 0
		self.accessory0 = 0