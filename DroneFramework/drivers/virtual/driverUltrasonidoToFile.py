_autor_ = "Jorge R. Encinas"
import cpuinfo, time

info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # Rec sensor running in Raspberry PI
    import RPi.GPIO as GPIO

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    TRIGGER = 22
    ECHO = 18
    GPIO.setup(TRIGGER, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIGGER, False)
    try:
        f = open('sensorUltrasonico.gpio.serial.new', 'w')
        # start = time.time()
        while True:
            print "recording sensors"
            print "-----------------"
            GPIO.output(TRIGGER, True)
            time.sleep(0.00001)
            GPIO.output(TRIGGER, False)
            while GPIO.input(ECHO) == 0:
                start = time.time()
            while GPIO.input(ECHO) == 1:
                stop = time.time()
            elapsed = stop - start
            distance = round((elapsed * 34300) / 2, 3)
            print distance
            f.write('distance: ' + str(distance) + ' elapsed: ' + str(elapsed) + '\n')
            # time.sleep(0.02)
    except KeyboardInterrupt:
        print "\nKeyboard interrupt and cleanup gpio"
        GPIO.cleanup()
        f.close()
else:
    print 'Debe ejecutar en una raspberry para grabar, primero debe instalar el ultrasonico en los pines' \
          'TRIGGER = 22  ECHO = 18'
