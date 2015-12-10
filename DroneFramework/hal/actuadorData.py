_autor_ = "I.C.C"

import abc
from abc import ABCMeta


class ActuadorData(object):
    __metaclass__ = ABCMeta

    @abc.abstractmethod
    def setData(self,data):
        # pone los datos que debe manejar el actuador
         raise NotImplementedError( "Should have implemented this" )

    @abc.abstractmethod
    def getData(self):
        # recupera los datos del actuador
         raise NotImplementedError( "Should have implemented this" )


