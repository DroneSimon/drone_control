from actuadorData import ActuadorData

class ActuadorDataMotor(ActuadorData):

    def __init__(self, data):
        """
        :type data Dictionary
        """

        #sensorData
        self.data = data


    def getData(self):
        # devuelve datos del motor
        return self.data

    def setData(self, data):
        self.data = data

