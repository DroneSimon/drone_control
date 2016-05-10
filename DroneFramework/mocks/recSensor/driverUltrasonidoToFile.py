# Refactor Jorge Encinas
import RPi_porsi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
mode=GPIO.getmode
TRIGGER = 22
ECHO    = 18
GPIO.setup(TRIGGER,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIGGER,False)
#start 

try:
    f = open('sensorUltrasonico.gpio', 'w')
    #start = time.time()
    while True:
        print "recording sensors"
        print "-----------------"
        GPIO.output(TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER,False)
        while GPIO.input(ECHO)==0:
        
        start = time.time()
        while GPIO.input(ECHO)==1:
        
        stop = time.time()
        elapsed = stop - start
        distance =round((elapsed * 34300)/2, 3)
        print distance
        f.write('distance: ' + str(distance)+  ' elapsed: ' + str(elapsed) + '\n')
        # time.sleep(0.02)
except KeyboardInterrupt:
    print "\nKeyboard interrupt and cleanup gpio"
    GPIO.cleanup()
    f.close()


#modified by Diego Garcia
from driver import Driver
class DriverUltrasonido(Driver):

    def getData(self):

        GPIO.output(TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER,False)
        start = time.time()
        stop = None
        while GPIO.input(ECHO)==0:
            start = time.time()
        while GPIO.input(ECHO)==1:
            stop = time.time()
        elapsed = stop-start
        distance =(elapsed * 34300)/2

        return {'altura' : distance}

    def getStatus(self):
        # tiene los datos del sensor
        # ok, no_ok, excepcion,
        raise NotImplementedError( "Should have implemented this" )

    @property
    def forceRead(self):
        # fuerza a hacer una nueva lectura al sensor
		return self.getData()

    def reset(self):
        # inicializa datos sensor
        raise NotImplementedError( "Should have implemented this" )
