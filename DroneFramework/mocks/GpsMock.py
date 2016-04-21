import mock.py

def test():
  from mock import MagicMock
  sensorGPS = MagicMock(return_value=['Altitud: 100','Longitud: 50'])
  print sensorGPS.return_value
  sensorGPS(return_altitude='35')
