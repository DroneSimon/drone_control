class Serial():
    def __init__(self, port, baudrate,timeout=1):
        print "serial.Serial que no debe llamarse en la raspberry, pero se necesita el momento del import para que corran las pruebas"

    def readline(self):
        return "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
    def write(self, text):
        return "$GPGGA,232847.727,1723.6149,S,06608.8126,W,1,03,5.6,2602.8,M,28.8,M,,0000*6D"
