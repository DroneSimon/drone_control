#!/usr/bin/python
_autor_ = "Jorge R. Encinas"
import cpuinfo

info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # Rec sensor running in Raspberry PI

    import smbus
    import math, time, os

    # Power management registers
    power_mgmt_1 = 0x6b
    power_mgmt_2 = 0x6c


    def read_byte(adr):
        return bus.read_byte_data(address, adr)


    def read_word(adr):
        high = bus.read_byte_data(address, adr)
        low = bus.read_byte_data(address, adr + 1)
        val = (high << 8) + low
        return val


    def read_word_2c(adr):
        val = read_word(adr)
        if (val >= 0x8000):
            return -((65535 - val) + 1)
        else:
            return val


    def dist(a, b):
        return math.sqrt((a * a) + (b * b))


    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)


    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)


    try:
        f = open('sensorGiroscopio.i2c.serial.new', 'w')
        while 1:
            bus = smbus.SMBus(1)  # or bus = smbus.SMBus(1) for Revision 2 boards
            address = 0x68  # This is the address value read via the i2cdetect command

            # Now wake the 6050 up as it starts in sleep mode
            bus.write_byte_data(address, power_mgmt_1, 0)

            print "recording sensors"
            print "-----------------"
            print "gyro data"
            print "---------"

            gyro_xout = read_word_2c(0x43)
            gyro_yout = read_word_2c(0x45)
            gyro_zout = read_word_2c(0x47)

            print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
            print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
            print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
            f.write('gyro_xout: ' + str(gyro_xout) + '\n')
            f.write('gyro_yout: ' + str(gyro_xout) + '\n')
            f.write('gyro_zout: ' + str(gyro_zout) + '\n')
            f.write('gyro_xout_scaled: ' + str(gyro_xout / 131) + '\n')
            f.write('gyro_yout_scaled: ' + str(gyro_yout / 131) + '\n')
            f.write('gyro_zout_scaled: ' + str(gyro_zout / 131) + '\n')

            print
            print "accelerometer data"
            print "------------------"

            accel_xout = read_word_2c(0x3b)
            accel_yout = read_word_2c(0x3d)
            accel_zout = read_word_2c(0x3f)
            accel_xout_scaled = accel_xout / 16384.0
            accel_yout_scaled = accel_yout / 16384.0
            accel_zout_scaled = accel_zout / 16384.0
            f.write('accel_xout: ' + str(gyro_xout) + '\n')
            f.write('accel_yout: ' + str(gyro_xout) + '\n')
            f.write('accel_zout: ' + str(gyro_zout) + '\n')
            f.write('accel_xout_scaled: ' + str(gyro_xout / 131) + '\n')
            f.write('accel_yout_scaled: ' + str(gyro_yout / 131) + '\n')
            f.write('accel_zout_scaled: ' + str(gyro_zout / 131) + '\n')

            print "accel_xout: ", str(accel_xout), " scaled: ", accel_xout_scaled
            print "accel_yout: ", str(accel_yout), " scaled: ", accel_yout_scaled
            print "accel_zout: ", str(accel_zout), " scaled: ", accel_zout_scaled

            print "x rotation: ", get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
            print "y rotation: ", get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)

            f.write(
                'x_rotation: ' + str(get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)) + '\n')
            f.write(
                'y_rotation: ' + str(get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)) + '\n')

            """
            gyro_xout = read_word_2c(0x43)
            gyro_yout = read_word_2c(0x45)
            gyro_zout = read_word_2c(0x47)

            print "gyro_xout: ", gyro_xout, " scaled: ", (gyro_xout / 131)
            print "gyro_yout: ", gyro_yout, " scaled: ", (gyro_yout / 131)
            print "gyro_zout: ", gyro_zout, " scaled: ", (gyro_zout / 131)
            """
            time.sleep(.1)
            os.system("clear")

    except KeyboardInterrupt:
        print "MPU  ->  finalizado"
        f.close()
else:
    print 'Debe ejecutar en una raspberry para grabar, primero debe instalar el Giroscopio en el bus i2c'