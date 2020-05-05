import sqlite3
import sys
import time
import RPi.GPIO as GPIO

pin = 8
eventReading = False

GPIO.setmode(GPIO.BOARD)    
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def log_values():
	conn=sqlite3.connect('/var/www/lab_app/proj_app.db')  #It is important to provide an
							    						  #absolute path to the database
							    						  #file, otherwise Cron won't be
							     						  #able to find it!
	curs=conn.cursor()
	curs.execute("""INSERT INTO mosquitoReadings VALUES(datetime(CURRENT_TIMESTAMP, 'localtime')
				)""",)
	conn.commit()
	conn.close()

while eventReading == False:
    if(GPIO.input(pin) == 0):
     log_values()
     time.sleep(1)
     eventReading == True
