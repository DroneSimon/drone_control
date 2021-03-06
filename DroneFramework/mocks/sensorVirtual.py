_autor_ = "Jorge R. Encinas"
from time import sleep
import threading, os, re, pynmea2

CONST_GYROSCOPE = 0
CONST_MAGNETOMETER = 1
CONST_ULTRASONIC = 2
CONST_GPS = 3

class SensorVirtual(threading.Thread):
	"""docstring for SensorVirtual
	instantiate with these parameters
	SensorVirtual([ 'giroscopio' or 'magnetometro' or 'ultrasonico or' gps], [file to open])"""
	def __init__(self, name, file):
		threading.Thread.__init__(self)
		self.name = name
		self.file = file
		self.data = None
		self.readFile = True
		self.gps = [.0,.0,.0]
	    
	def run(self):
		self.readFile = True
		self.simulateSensor()

	def simulateSensor(self):
		try:
			if os.stat(self.file).st_size > 0:
				f = open(self.file,'r')
				while self.readFile:
					line = f.readline()
					if line == '':
						f.seek(0)
						line = f.readline()
					self.data = self.getDataTypeSensor(line,f) 
				f.close()
			else:
				print 'El archivo '+ self.file + ' esta vacio'
		except KeyboardInterrupt:
			print 'Interrumpido por el teclado, archivo cerrado'
			f.close()
		except (IOError, WindowsError) as e:
			print 'El archivo '+ self.file + ' no esta en el directorio, ' + str(e.strerror)

	def stop(self):
		self.readFile = False

	def getRunStatus(self):
		return self.readFile

	
	def getData(self):
		""" while the sensor is simulated.
		you can get the data generated in an instant of time prerecorded.

		Returns string if GPS instantiated,
		Vector containing int and float if an instance is created gyroscope
		 and the position [12] contains rotation in X and [13] rotation in Y,
		float if Ultrasonic instantiated,
		float if Magnetometer instantiated."""
		return self.data

	def getDataTypeSensor(self, line,f):
		if self.name == 'giroscopio': # for sensorGiroscopio, acelerometer MPU6050
			gyro_xout = int(line.split(' ')[1])
			gyro_yout = int(f.readline().split(' ')[1])
			gyro_zout = int(f.readline().split(' ')[1])
			gyro_xout_scaled = int(f.readline().split(' ')[1])
			gyro_yout_scaled = int(f.readline().split(' ')[1])
			gyro_zout_scaled = int(f.readline().split(' ')[1])
			accel_xout = int(f.readline().split(' ')[1])
			accel_yout = int(f.readline().split(' ')[1])
			accel_zout = int(f.readline().split(' ')[1])
			accel_xout_scaled = int(f.readline().split(' ')[1])
			accel_yout_scaled = int(f.readline().split(' ')[1])
			accel_zout_scaled = int(f.readline().split(' ')[1])
			x_rotation = float(f.readline().split(' ')[1])
			y_rotation = float(f.readline().split(' ')[1])
			line = [gyro_xout, gyro_yout, gyro_zout, 
					gyro_xout_scaled, gyro_yout_scaled, gyro_zout_scaled, #scaled
					accel_xout, accel_yout, accel_zout, 
					accel_xout_scaled, accel_yout_scaled, accel_zout_scaled, #scaled
					x_rotation, y_rotation] # array [12] [13]
			sleep( .1 )

		if self.name == 'magnetometro': # for sensorMagnetometro HMC5883L
			line = float(line.split(' ')[1])
			sleep(.2)

		if self.name == 'ultrasonico': # for sensorUltrasonico HC-SR04 4Mt
			gpioData = line.split(' ')
			line = float(gpioData[1])
			sleep( float(gpioData[3]) )

		if self.name == 'gps':
			gps = pynmea2.parse(line)
			try:
				self.gps[0]=gps.latitude
			except AttributeError as e:
				# print(e)
				pass
			try:
				self.gps[1]=gps.longitude
			except AttributeError as e:
				# print(e)
				pass 
			try:
				self.gps[2]=gps.altitude
			except AttributeError as e:
				# print(e)
				pass
			line = self.gps
			sleep(.1)
		return line

def testSensorFiles():
	fileMagnetometer = 'sensorMagnetometro.i2c.serial'
	fileGyroscope = 'sensorGiroscopio.i2c.serial'
	fileUltrasonic = 'sensorUltrasonico.gpio.serial'
	fileGPS = 'gpsDataCaptured.serial'

	threadMagetometro = SensorVirtual('magnetometro', fileMagnetometer)
	threadGyroscope = SensorVirtual('giroscopio', fileGyroscope)
	threadUltrasonic = SensorVirtual('ultrasonico', fileUltrasonic)
	threadGPS = SensorVirtual('gps', fileGPS)
	try:
		print 'test magnetometro'
		threadMagetometro.start()
		for i in range(3):
			sleep(1)
			print threadMagetometro.getData()
		threadMagetometro.stop()
		print 'test giroscopio'
		threadGyroscope.start()
		for i in range(3):
			sleep(1)
			print threadGyroscope.getData()
		threadGyroscope.stop()
		print 'test ultrasonico'
		threadUltrasonic.start()
		for i in range(3):
			sleep(1)
			print threadUltrasonic.getData()
		threadUltrasonic.stop()
		print 'test GPS'
		threadGPS.start()
		for i in range(3):
			sleep(1)
			print threadGPS.getData()
		threadGPS.stop()
	except KeyboardInterrupt:
		if threadMagetometro.getRunStatus():
			threadMagetometro.stop()
			print 'magnetometro desconectado'
		if threadGyroscope.getRunStatus():
			threadGyroscope.stop()
			print 'giroscopio desconectado'
		if threadUltrasonic.getRunStatus():
			threadUltrasonic.stop()
			print 'ultrasonico desconectado'
		if threadGPS.getRunStatus():
			threadGPS.stop()
			print 'gps desconectado'
	finally:
		print 'test de archivos realizados correctamente'
		
if  __name__ =='__main__':
    testSensorFiles()
