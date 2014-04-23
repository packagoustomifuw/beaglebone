#!/usr/bin/python

import Adafruit_BBIO.GPIO as GPIO
import time

sw1 = "P9_12"
GPIO.setup(sw1, GPIO.IN)

try:

	while True:
		#GPIO.wait_for_edge(sw1,GPIO.RISING)
		GPIO.add_event_detect(sw1, GPIO.RISING)
		if GPIO.event_detected(sw1):
			print "pressed"
		#GPIO.wait_for_edge(sw1,GPIO.FALLING)
		#GPIO.add_event_detect(sw1, GPIO.FALLING)
		#if GPIO.event_detected(sw1):
		#	print "released"

except KeyboardInterrupt:
	print "User exited program by Ctrl+C.\n"
	GPIO.cleanup()

