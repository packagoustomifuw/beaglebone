#!/usr/bin/python

#import the Adafruit beaglebone IO library for GPIO
import Adafruit_BBIO.GPIO as GPIO
#import the Adafruit PWM library
import Adafruit_BBIO.PWM as PWM
#import the time library
import time
import math

button = "P8_11"

#Setup P8 pin 11 as input
GPIO.setup(button, GPIO.IN)


while True:

	def alternate():

		#Setup P8 pins 10 and 12 as output
		GPIO.setup("P8_10", GPIO.OUT)
		GPIO.setup("P8_12", GPIO.OUT)

		#begin loop
		while True:
			x = 1.0
			while x < 1001:
			#turn on LED
				if x % 2 == 0:
					GPIO.output("P8_12", GPIO.HIGH)
					GPIO.output("P8_10", GPIO.LOW)
				else:
					GPIO.output("P8_12", GPIO.LOW)
					GPIO.output("P8_10", GPIO.HIGH)
				#delay
				time.sleep(3/x)
				x += 1
				GPIO.add_event_detect(button, GPIO.RISING)
				GPIO.add_event_callback(button, off)
			while x > 0:
				if x % 2 == 0:
        	                        GPIO.output("P8_12", GPIO.HIGH)
                	                GPIO.output("P8_10", GPIO.LOW)
                        	else:
	                                GPIO.output("P8_12", GPIO.LOW)
        	                        GPIO.output("P8_10", GPIO.HIGH)
                	        #delay
                        	time.sleep(3/x)
	                        x -= 1
				GPIO.add_event_detect(button, GPIO.RISING)
                                GPIO.add_event_callback(button, off)

	def off():
		#Setup P8 pins 10 and 12 as output
	        GPIO.setup("P8_10", GPIO.OUT)
        	GPIO.setup("P8_12", GPIO.OUT)
		GPIO.output("P8_12", GPIO.LOW)
		GPIO.output("P8_10", GPIO.LOW)


	GPIO.add_event_detect(button, GPIO.RISING)
	if GPIO.event_detected(button):
		GPIO.add_event_callback(button, alternate)
