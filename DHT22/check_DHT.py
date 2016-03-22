#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Original DHT Sensor Code from : https://github.com/adafruit/Adafruit_Python_DHT

# Python 2.7 req

import sys, argparse
import Adafruit_DHT

# Dict of sensor types, proper names
sensor_types = { '11': Adafruit_DHT.DHT11,
	'22': Adafruit_DHT.DHT22,
	'2302': Adafruit_DHT.AM2302 }

parser = argparse.ArgumentParser()

parser.add_argument('-s', action="store", dest="sensor", type=int)
parser.add_argument('-p', action="store", dest="pin", type=int)
parser.add_argument('-t', action="store", dest="type")
parser.add_argument('-w', action="store", dest="warn", type=int)
parser.add_argument('-c', action="store", dest="crit", type=int)
args = parser.parse_args();

####################
# s = sensor type
# p = GPIO pin#
# t = type of output
# w = warning level
# c = critcal level
###################

if args.sensor is not None and args.pin is not None and args.type is not None and args.warn is not None and args.crit is not None:
	sensor = sensor_types['{}'.format(args.sensor)]
	pin='{}'.format(args.pin)
	type='{}'.format(args.type)
	warn='{}'.format(args.warn)
	crit='{}'.format(args.crit)

	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

	# Un-comment the line below to convert the temperature to Fahrenheit.
	# temperature = temperature * 9/5.0 + 32
	
	if type == 'temp':
		tempVal='{0:0.1f}'.format(temperature)
		if tempVal < warn and tempVal < crit:
			print 'OK - Temperature is %s*|Temperature=%s*;%s;%s;;' % (tempVal, tempVal, warn, crit)
			sys.exit(0) # OK
		elif tempVal > warn and tempVal < crit:
			print 'WARN - Temperature is %s*|Temperature=%s*;%s;%s;;' % (tempVal, tempVal, warn, crit)
			sys.exit(1) # WARN
		elif tempVal > warn and tempVal > crit:
			print 'CRITICAL - Temperature is %s*|Temperature=%s*;%s;%s;;' % (tempVal, tempVal, warn, crit)
			sys.exit(2) # CRITICAL
		else:
			print 'UNKNOWN - Temperature is %s*|Temperature=%s*;%s;%s;;' % (tempVal, tempVal, warn, crit)
			sys.exit(3) # UNKNOWN
	elif type == 'humid':
		humidVal='{0:0.1f}'.format(humidity)
		if humidVal < warn and humidVal < crit:
			print 'OK - Humidity is %s%%|Humidity=%s%%;%s;%s;;' % (humidVal, humidVal, warn, crit)
			sys.exit(0) # OK
		elif humidVal > warn and humidVal < crit:
			print 'WARN - Humidity is %s%%|Humidity=%s%%;%s;%s;;' % (humidVal, humidVal, warn, crit)
			sys.exit(1) # WARN
		elif humidVal > warn and humidVal > crit:
			print 'CRITICAL - Humidity is %s%%|Humidity=%s%%;%s;%s;;' % (humidVal, humidVal, warn, crit)
			sys.exit(2) # CRITICAL
		else:
			print 'UNKNOWN - Humidity is %s%%|Humidity=%s%%;%s;%s;;' % (humidVal, humidVal, warn, crit)
			sys.exit(3) # UNKNOWN
	elif type == 'debug':
		print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
		sys.exit(3)
	else:
		print 'shouldnt be here'
		sys.exit(3) # UNKNOWN

else:
	#DEBUG print '{}|{}|{}|{}|{}'.format(sensor, pin, type, warn, crit)
	print("Usage: sudo ./script.py -s [11|22|2302] -p GPIOpin# -t OutputType|debug -w Warn -c Crit")
	sys.exit(3)
