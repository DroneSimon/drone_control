import abc
from abc import ABCMeta

from drivers.driver import Driver


class SensorData(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def getAge(self):
        # devuelve la antiguedad de los datos
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getData(self):
        # tiene los datos del sensor
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def setAge(self, age):
        # tiene los datos del sensor
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def setData(self, data):
        # tiene los datos del sensor
        raise NotImplementedError( "Should have implemented this" )





