import RPi.GPIO as GPIO
from picamera import PiCamera
import time
from PIL import Image

camera = PiCamera()

camera.start_preview()
time.sleep(2)
camera.stop_preview()
def button_callback( channel ):
    print('button')
    camera.capture('test.jpg')
    im = Image.open(r'test.jpg')
    im.show()
    

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
