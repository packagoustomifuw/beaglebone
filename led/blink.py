#!/usr/bin/python

#import the Adafruit beaglebone IO library for GPIO
import Adafruit_BBIO.GPIO as GPIO
#import the Adafruit PWM library
import Adafruit_BBIO.PWM as PWM
#import the time library
import time
import math

#Setup P8 pins 10 and 12 as output
GPIO.setup("P8_10", GPIO.OUT)
GPIO.setup("P8_12", GPIO.OUT)
#Setup P8 pin 11 as input
GPIO.setup("P8_11", GPIO.IN)

#begin loop
while True:
	#check if switch is pressed
	if GPIO.input("P8_11"):
		#start the for loop
		#GPIO.output("P8_10", GPIO.HIGH)
		#GPIO.output("P8_12", GPIO.HIGH)
		x = 1.0
		while x < 1001:
			#if pressed, turn on LED
			if x % 2 == 0:
				GPIO.output("P8_12", GPIO.HIGH)
				GPIO.output("P8_10", GPIO.LOW)
			else:
				GPIO.output("P8_12", GPIO.LOW)
				GPIO.output("P8_10", GPIO.HIGH)
			#delay
			time.sleep(3/x)
			#time.sleep(10/math.exp(x))
			#TODO: make this increase exponentially
			x += 1
	else:
		#if not pressed, leave LED off
		GPIO.output("P8_12", GPIO.LOW)
		GPIO.output("P8_10", GPIO.LOW)
