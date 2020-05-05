import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) # use board numbers
# define input pin
pin = 10
GPIO.setup(pin, GPIO.IN)

while 1:
  if GPIO.input(pin) == GPIO.HIGH:
    print "Mosquito Detected!"
    time.sleep(5)
