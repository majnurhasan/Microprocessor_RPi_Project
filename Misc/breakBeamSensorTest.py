import time
import RPi.GPIO as GPIO
pin = 8

GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while 1:
    if(GPIO.input(pin) == 0):
     print("Beam Broken")
     time.sleep(1)
    

    
    
