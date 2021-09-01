import time
import RPi.GPIO as GPIO

import globals

def btn_pressed(pin):
    if(GPIO.input(pin) == False):
        name = ('output/'+str(int(time.time()))+'.jpg')
        globals.camera.stop_recording()
        globals.camera.resolution = (2592, 1944)
        globals.camera.capture(name)
        globals.camera.resolution = (480, 320)
        globals.camera.start_recording(output, format='mjpeg')
        print('captured', name)

def init():
    BTN_PIN = 4

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(BTN_PIN, GPIO.RISING, callback=btn_pressed)
