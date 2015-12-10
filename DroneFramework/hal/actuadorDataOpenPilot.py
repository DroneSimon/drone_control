_autor_ = "I.C.C."

from actuadorData import ActuadorData



class ActuadorDataOpenPilot(ActuadorData):

    def __init__(self, data):
        """
        :type data Diccionario
        """
        #sensorData = {'roll':0,  'pitch':0, 'tortle':0,'yaw':0, 'modoVuelo':estabilizado/acrobatico/ rate (ratios. hasta 6), 'prendido':si/no}
        self.data = data


    def getData(self):
        # tiene los datos del sensor
        return self.data


    def setData(self, data):

        self.data = data


