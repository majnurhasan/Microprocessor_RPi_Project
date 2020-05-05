from flask import Flask, request, render_template
import time
import datetime
import sqlite3
import sys
import Adafruit_DHT

app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lab_temp")
def lab_temp():
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
	if humidity is not None and temperature is not None:
		return render_template("lab_temp.html",temp=temperature,hum=humidity)
	else:
		return render_template("no_sensor.html")

@app.route("/proj_env_db", methods=['GET'])
def proj_env_db():
	mosquitoReadings, dailyReadings, from_date_str, to_date_str = get_records()
	return render_template("proj_env_db.html", mosReadings		= mosquitoReadings, 
											   daiReadings		= dailyReadings,
											   from_date 		= from_date_str,
											   to_date			= to_date_str,
											   dai_items		= len(dailyReadings))

def get_records():
	from_date_str 	= request.args.get('from',time.strftime("%Y-%m-%d")) #Get the from date value from the URL
 	to_date_str 	= request.args.get('to',time.strftime("%Y-%m-%d"))   #Get the to date value from the URL
	
	if not validate_date(from_date_str):	
		from_date_str 	= time.strftime("%Y-%m-%d")
	if not validate_date(to_date_str):
		to_date_str 	= time.strftime("%Y-%m-%d")
	
	conn=sqlite3.connect('/var/www/lab_app/proj_app.db')
	curs=conn.cursor()
	curs.execute("SELECT * FROM mosquitoReadings WHERE rDatetime BETWEEN ? AND ?", (from_date_str, to_date_str))
	mosquitoReadings = curs.fetchall()
	curs.execute("SELECT * FROM dailyReadings WHERE rDate BETWEEN ? AND ?", (from_date_str, to_date_str))
	dailyReadings = curs.fetchall()
	conn.close()
	return [mosquitoReadings, dailyReadings, from_date_str, to_date_str]

def validate_date(d):
    try:
        datetime.datetime.strptime(d, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
