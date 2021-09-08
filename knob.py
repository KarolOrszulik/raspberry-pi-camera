import RPi.GPIO as GPIO
import globals

_pinA = 20
_pinB = 16

counter = 0

valid_isos = [100, 200, 400, 800]

def handle_knob(pin):
    global counter

    _stateA = GPIO.input(_pinA)
    _stateB = GPIO.input(_pinB)

    counter += 1 if _stateA == _stateB else -1

    globals.camera.iso = valid_isos[counter%len(valid_isos)]
    print(globals.camera.iso)


def init():
    GPIO.setup(_pinA, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(_pinB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.add_event_detect(_pinA, GPIO.BOTH, callback=handle_knob, bouncetime=30)
    print("Knob initialised")
