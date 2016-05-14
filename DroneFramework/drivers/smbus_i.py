class SMBus():
    def __init__(self, port):
        print "smbusl.SMBus que no debe llamarse en la raspberry, pero se necesita el momento del import para que corran las pruebas"

    def read_byte_data(self, address, adr):
        return "Bearing: 88.4859266394"

    def write_byte_data(self, address, adr, value):
        return "write del smbus mock"
