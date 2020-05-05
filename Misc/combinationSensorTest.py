import time
import RPi.GPIO as GPIO
breakBeamSensorPin = 8
soundSensorPin = 10
hasPassed = 0

GPIO.setmode(GPIO.BOARD)    
GPIO.setup(breakBeamSensorPin, GPIO.IN)
GPIO.setup(soundSensorPin, GPIO.IN)

while 1:
    if(GPIO.input(breakBeamSensorPin) == 0):
     print("Insect Passed") #database access to insectPassed
     hasPassed = 1
     time.sleep(1)

    if(GPIO.input(soundSensorPin) == 1):
     if(hasPassed == 1):
         print("Mosquito Detected") #database access to mosquitoDetected
         hasPassed = 0
         time.sleep(1)

        
    
    
    
