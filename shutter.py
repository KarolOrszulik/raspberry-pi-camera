import RPi.GPIO as GPIO
import globals
import time

_btnpin = 21

def btn_pressed(pin):
    if(GPIO.input(pin) == False):
        name = ('output/'+str(int(time.time()))+'.jpg')
        globals.camera.stop_recording()
        globals.camera.resolution = (2592, 1944)
        globals.camera.capture(name)
        globals.camera.resolution = (480, 320)
        globals.camera.start_recording(globals.output, format='mjpeg')
        print('captured', name)

def init():
    GPIO.setup(_btnpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(_btnpin, GPIO.RISING, callback=btn_pressed, bouncetime=30)
    print("Shutter initialised")
