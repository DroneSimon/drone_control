import random

import time

BOARD="BOARD"
getmode="getmode"
OUT="out"
IN="IN"
contador=3

def setwarnings(true_false):
        return "se llamo setwarning"

def setmode( value):
        return "write del smbus mock"

def setup(gpio_trigger,gpio_out):
        return "setup"

def input(contador_1):
        time.sleep(0.01)
        global contador
        contador=contador+1
        a=contador % 3.0
        if a==0:
                return 0
        return 1

def output(gpio_trigger, false_true):
        return "ouput"


