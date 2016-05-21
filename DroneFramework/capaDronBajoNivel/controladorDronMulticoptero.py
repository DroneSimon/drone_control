from DroneFramework.drivers.driverGiroscopio import DriverGiroscopio

_autor_= "I.C.C."

import time
from DroneFramework.hal.actuadorOpenPilot import ActuadorOpenPilot

from DroneFramework.hal.sensorGPS import SensorGPS
from DroneFramework.hal.sensorGiroscopio import SensorGiroscopio
from DroneFramework.hal.sensorUltrasonido import SensorUltrasonido
from DroneFramework.hal.sensorMagnetometro import SensorMagnetometro
from DroneFramework.hal.sensorBateria import SensorBateria


import cpuinfo
raspberry = False
info = cpuinfo.get_cpu_info()
if info['arch'] == 'ARM_7':  # test sensor running in Raspberry PI
    from DroneFramework.drivers.driverGPS import DriverGPS
    from DroneFramework.drivers.driverMagnetometro import DriverMagnetometro
    from DroneFramework.drivers.driverUltrasonido import DriverUltrasonido
    from DroneFramework.drivers.driverGiroscopio import DriverGiroscopio
    raspberry = True
else:
    from DroneFramework.drivers.virtual.driverMagnetometroVirtual import DriverMagnetometroVirtual as DriverMagnetometro
    from DroneFramework.drivers.virtual.driverUltrasonidoVirtual import DriverUltrasonidoVirtual as DriverUltrasonido
    from DroneFramework.drivers.virtual.driverGPSvirtual import  DriverGPSvirtual as DriverGPS
    from DroneFramework.drivers.virtual.driverGiroscopioVirtual import DriverGiroscopioVirtual as DriverGiroscopio
# falta driver de nivel de bateria


from controladorDronVolador import ControladorDronVolador

class ControladorDronMulticoptero(ControladorDronVolador):

    def __init__(self):
        self.actuadorOP= ActuadorOpenPilot()

        self.sensorMagnetometro = SensorMagnetometro(DriverMagnetometro())
        self.sensorGiroscopio=SensorGiroscopio(DriverGiroscopio())
        self.sensorGPS=SensorGPS(DriverGPS())
        #self.sensorBateria= SensorBateria()

        self.alcanceUltrasonido=4000
        self.sensorUltrasonido = SensorUltrasonido(DriverUltrasonido(), self.alcanceUltrasonido)

        #self.sensorGPS=SensorGPS(DriverGPS())
        # convierto la info del GPS a centimetros porque viene en metros
        self.altitudSuelo=self.sensorGPS.getLastInfo().getData()['altitud']*100

        # para yaw, pitch, roll
        self.velocidadMaxGiroOP=50  # arriba de 50 gira
        self.velocidadCeroGiroOP=50 # cuando esta 50 esta sin girar a ningun lado

        # para Throtle
        self.velocidadEstable=64
        self.velocidad10cm=30
        self.velocidad5cm=20
        self.velocidadMaxMotores=100
        self.distanciaMinimaDelSuelo=1  # 30 centimetros para aterrizar

        # angulo para avanzar
        self.anguloAvance=5

        # definicion de modos de vuelo
        self.modosDeOperacion={'estabilizado':0, 'acrobatico':1}    # esto hay que verificar


    # encender equivale a decir armar motores en OP
    def encender(self):
        self.actuadorOP.encender()

    #pone la altidud actual del GPS
    def setAltitudSuelo(self):
        self.altitudSuelo=self.sensorGPS.getLastInfo().getData()['altitud']

   # apagar equivale a decir que desarme motores en OP
    def apagar(self):
        self.actuadorOP.apagar()

    # giro lateral de la cabeza desde la pocision donde esta
    # velocidad es un entero de 1 al 50, no puede ser 0
    # si grados es negativo ira a la izquierda, sino a la derecha
    def yaw(self, grados, velocidad):
        anguloInicial=self.sensorMagnetometro.getAnguloCabezaDron()
        gradosAlcanzados=0

        direccion=1
        if (grados<0):
            direccion=-1

        grados=abs(grados)
        self.actuadorOP.setYaw(self.velocidadCeroGiroOP + velocidad*direccion)
        while (gradosAlcanzados<grados & velocidad>=1):
            gradosAlcanzados=abs(anguloInicial-self.sensorMagnetometro.getAnguloCabezaDron())
            time.sleep(.300)
        self.actuadorOP.setYaw(self.velocidadCeroGiroOP)

    # giro lateral de la cabeza a la izquierda desde la posicion donde esta
    def yaw_izquierda(self, grados, velocidad):
        self.yaw(-abs(grados),velocidad)

    # giro lateral de la cabeza a la derecha desde la pocision donde esta
    def yaw_derecha(self, grados, velocidad):
        self.yaw(abs(grados),velocidad)

    # elevar el dron: distancia estara en centimetros y es la distancia que debe subir desde donde esta
    # velocidad para elevarse debe ser mayor a velocidadEstable y menor a velocidadMaxMotores
    # velocidad se sumara a la velocidad estable - hasta velocidadMaxMotores
    def up(self, distancia, velocidad):

        distanciaInicial=self.getDistanciaSuelo()
        distanciaAlcanzada=distanciaInicial
        distanciaFinal=distanciaInicial+distancia

        # el throtle es la velocidad de los motores
        velocidad=self.velocidadEstable+velocidad
        if(velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada<distanciaFinal & velocidad>self.velocidadEstable):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)
        self.actuadorOP.setThrotle(self.velocidadEstable)

    # bajar el dron hasta "distancia" del piso. Estara en centimetros
    # velocidad tendria que ser menor a la estable si es mayor la dejo en velocidad estable, e.d. no baja
    def down(self, distancia, velocidad):
        if (velocidad>self.velocidadEstable):
            velocidad= self.velocidadEstable

        distanciaInicial=self.getDistanciaSuelo()
        distanciaAlcanzada=distanciaInicial
        distanciaFinal=distancia

        if (distanciaFinal<30):
            distanciaFinal=30

        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>distanciaFinal & velocidad<self.velocidadEstable):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)
        self.actuadorOP.setThrotle(self.velocidadEstable)

    # me devuelve la distancia del dron al suelo, si esta fuera del alcance del ultrasonido devuelve
    # distancia GPS. para ello se debera setear 1ro distancia altitud suelo
    def getDistanciaSuelo(self):
        distanciaSuelo=self.sensorUltrasonido.getLastInfo()['altura']
        if (distanciaSuelo>=self.alcanceUltrasonido):
            distanciaSuelo=self.sensorGPS.getLastInfo()['altitud']*100-self.altitudSuelo
        return distanciaSuelo

    def aterrizar1(self):
        self.nivelarDron()
        self.down(30,self.velocidadEstable/2)
        self.down(10,self.velocidad10cm)
        self.down(5,self.velocidad5cm)
        self.apagar()

    def aterrizar2(self):
        distanciaInicial=self.getDistanciaSuelo()
        distanciaAlcanzada=distanciaInicial

        velocidad= self.velocidadEstable * 0.8
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>40 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)

        velocidad= self.velocidadEstable / 2
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>10 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)

        velocidad=self.velocidad10cm
        self.actuadorOP.setThrotle(velocidad)
        while (distanciaAlcanzada>5 ):
             distanciaAlcanzada=self.getDistanciaSuelo()
             time.sleep(.300)

        self.actuadorOP.setThrotle(self.velocidad5cm)
        time.sleep(.300)
        self.actuadorOP.setThrotle(self.velocidad5cm/2)
        self.apagar()

    # cabeceo - elevacion de la cabeza la sube/baja a los "grados" indicados en "y" del giroscopio
    # a la velocidad(0-50) indicada
    def pitch_arriba(self, grados, velocidad):
        grados=-abs(grados) # porque el "angulo y" hacia arriba es negativo
        y= self.sensorGiroscopio.getLastInfo().getData()['y']
        if (velocidad>50):
            velocidad=50

        direccion=1 #subir
        if (y<grados):
            direccion=-1 #bajar

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP+velocidad*direccion)
        while ( y<grados & velocidad>0  & direccion==-1 ):   #bajar
           y= self.sensorGiroscopio.getLastInfo().getData()['y']
           time.sleep(.300)

        while ( y>grados & velocidad>0  & direccion==1 ):   #subir
           y= self.sensorGiroscopio.getLastInfo().getData()['y']
           time.sleep(.300)

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP)

    # cabeceo - bajar la cabeza, baja los "grados" en y de giroscopio a la velocidad (1-50) indicada
    def pitch_abajo(self, grados, velocidad):

        grados=abs(grados) # porque el "angulo y" hacia abajo es positivo

        y= self.sensorGiroscopio.getLastInfo().getData()['y']
        if (velocidad>50):
            velocidad=50

        direccion=1 #subir
        if (y<grados):
            direccion=-1 #bajar

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP+velocidad*direccion)

        while ( y<grados & velocidad>0  & direccion==-1 ):   #bajar
           y= self.sensorGiroscopio.getLastInfo().getData()['y']
           time.sleep(.300)

        while ( y>grados & velocidad>0  & direccion==1 ):   #subir
           y= self.sensorGiroscopio.getLastInfo().getData()['y']
           time.sleep(.300)

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP)

    # giro lateral de costado a la derecha: x giroscopio positivo
    # deja el dron en "grados" a la derecha a la "velocidad" indicada
    def roll_derecha(self, grados, velocidad):
        grados=abs(grados) # porque el "angulo x" a la derecha es positivo

        x= self.sensorGiroscopio.getLastInfo().getData()['x']
        if (velocidad>50):
            velocidad=50

        direccion=1 #irA derecha
        if (x>grados):
            direccion=-1 #irA izquierda

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP+velocidad*direccion)

        while ( x<grados & velocidad>0  & direccion==1 ):   # irA a la derecha
           x= self.sensorGiroscopio.getLastInfo().getData()['x']
           time.sleep(.300)

        while ( x>grados & velocidad>0  & direccion==-1 ):   # irA a la izquierda
           x= self.sensorGiroscopio.getLastInfo().getData()['x']
           time.sleep(.300)
        self.actuadorOP.setPitch(self.velocidadCeroGiroOP)

    # giro lateral de costado a la izquierda
    # deja el dron en "grados" a la izquierda a la "velocidad" indicada
    def roll_izquierda(self, grados, velocidad ):
        grados=-abs(grados) # porque el "angulo x" a la izquierda es negativo

        x= self.sensorGiroscopio.getLastInfo().getData()['x']
        if (velocidad>50):
            velocidad=50

        direccion=1 #irA derecha
        if (x>grados):
            direccion=-1 #irA izquierda

        self.actuadorOP.setPitch(self.velocidadCeroGiroOP+velocidad*direccion)

        while ( x<grados & velocidad>0  & direccion==1 ):   # irA a la derecha
           x= self.sensorGiroscopio.getLastInfo().getData()['x']
           time.sleep(.300)

        while ( x>grados & velocidad>0  & direccion==-1 ):   # irA a la izquierda
           x= self.sensorGiroscopio.getLastInfo().getData()['x']
           time.sleep(.300)
        self.actuadorOP.setPitch(self.velocidadCeroGiroOP)

    # devuelve los angulos x, y z en un diccionario
    def getAnguloCabeza(self):
        return self.sensorGiroscopio.getLastInfo().getData()

    # devuelve x y z (longitud, latitud y altura al suelo en cm) como una tupla
    def getCoordenadas(self):
        xyz=self.sensorGPS.getCoordenadas()
        x=xyz['latitud']
        y=xyz['longitud']
        z=self.getDistanciaSuelo()
        return {'x':x,'y':y,'z':z}

    # avanza el dron en direccion a al acabeza
    def irAdelante(self, velocidad):
        velocidad=self.velocidadEstable+abs(velocidad)
        if (velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.nivelarDron()
        self.pitch_abajo(self.anguloAvance,5)
        self.actuadorOP.setThrotle(velocidad)

    # avanza el dron en direccion contraria a la cabeza
    def irAtras(self, velocidad):
        velocidad=self.velocidadEstable+abs(velocidad)
        if (velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.nivelarDron()
        self.pitch_arriba(self.anguloAvance,5)
        self.actuadorOP.setThrotle(velocidad)

    # avanza el dron hacia la derecha de su cabeza
    def irDerecha(self,velocidad):
        velocidad=self.velocidadEstable+abs(velocidad)
        if (velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.nivelarDron()
        self.roll_derecha(self.anguloAvance,5)
        self.actuadorOP.setThrotle(velocidad)

    # avanza el dron hacia la izquierda de su cabeza
    def irIzquierdad(self,velocidad):
        velocidad=self.velocidadEstable+abs(velocidad)
        if (velocidad>self.velocidadMaxMotores):
            velocidad=self.velocidadMaxMotores

        self.nivelarDron()
        self.roll_izquierda(self.anguloAvance,5)
        self.actuadorOP.setThrotle(velocidad)

    # pone el "x"  e "y" del giroscopio en 0
    def nivelarDron(self):
        self.pitch_abajo(0,5)
        self.roll_derecha(0,5)

    # estabilizado - acrobatico y tiene 6 modos mas
    def setModo(self,modo):
        self.actuadorOP.setModoVuelo(modo)

    def mantenerCoordenadas(self):
        self.nivelarDron()
        self.actuadorOP.setThrotle(self.velocidadEstable)

    # devuelve los valores de modos de vuelo en un diccionario:{'estabilizado', 'acrobatico'}
    def getModosDeOperacion(self):
        return self.modosDeOperacion

    def getStatus(self):
        return 'ok'

