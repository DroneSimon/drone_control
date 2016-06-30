import os
import os.path

class Imprime():
  def imprimir(self):
      return "la funcion patch:imprimir():"

def rm1(filename):
    i=Imprime()
    return (filename+' '+i.imprimir())

def rm(filename):

    if os.path.isfile(filename):
       print "encontro archivo y borra"
       os.remove(filename)

class RemovalService(object):
    """A service for removing objects from the filesystem."""
    print "dentro dela clase servicio"
    def rm(self,filename):
        print "dentro del metodo rm"
        if os.path.isfile(filename):
            os.remove(filename)

class UploadService(object):
    def __init__(self, removal_service1):
        print "inicializando el upload...."
        self.removal_serviceUS = removal_service1

    def upload_complete(self, filename):
        print "ejecutanto del borrado con el upload del servicio completado"
        self.removal_serviceUS.rm(filename)

class DummyClass:
    def hello(self):
        print("Hello world")
        return "OK"
