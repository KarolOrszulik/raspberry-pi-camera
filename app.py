import picamera

import globals
import camserver
import hardware_input

globals.init()


hardware_input.init()

globals.camera = picamera.PiCamera(resolution='480x320', framerate=24)

globals.output = camserver.StreamingOutput()

globals.camera.start_recording(globals.output, format='mjpeg')
try:
    server = camserver.StreamingServer(('', 8000), camserver.StreamingHandler)
    server.serve_forever()
finally:
    globals.camera.stop_recording()

