import abc
#Abstract Base Class todo son objetos en python y derivan de abc

from abc import ABCMeta


class Sensor(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def getLastInfo(self):
        # devuelve la informacion que tiene sensorData
        raise NotImplementedError( "Should have implemented this" )
        #print "get Last Info"

    @abc.abstractmethod
    def getStatus(self):
        #devuelve el estado del sensor
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def reset(self):
        #inicializa el sensor
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def forceRead(self):
        #obliga a leer al sensor
         raise NotImplementedError( "Should have implemented this" )

#sensor=Sensor()
#sensor.getLastInfo()