import RPi.GPIO as GPIO
import globals
import shutter
import knob

def init():
    GPIO.setmode(GPIO.BCM)

    shutter.init()
    knob.init()
