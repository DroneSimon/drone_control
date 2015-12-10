import Reconocedor_Fuego_Humo as fire_detector
import DroneFramework as drone

def anomalyDetect(img):
    detected = False;
    return fire_detector.detectar_fuego_humo(img)

def anomalyDetected():

    the_drone = drone.ControladorDronMulticoptero()
    the_drone.encender()
    the_drone.up(10, 0)
    the_drone.yaw(360, 10)
    the_drone.down(10,1)
    the_drone.apagar()

