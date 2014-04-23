#!/usr/bin/python

import time
import Adafruit_BBIO.PWM as PWM

#PWM init

PWM.start("P8_13", 0)
PWM.start("P8_19", 0)

while True:
	for i in range(0,100):
		PWM.set_duty_cycle("P8_13", float(i))
		#PWM.set_duty_cycle("P8_19", float(100-i))
		time.sleep(.01)

	for i in range(0,100):
		#PWM.set_duty_cycle("P8_13", float(i))
                PWM.set_duty_cycle("P8_13", float(100-i))
                time.sleep(.01)

	for i in range(0,100):
                PWM.set_duty_cycle("P8_19", float(i))
                #PWM.set_duty_cycle("P8_19", float(100-i))
                time.sleep(.01)

        for i in range(0,100):
                #PWM.set_duty_cycle("P8_13", float(i))
                PWM.set_duty_cycle("P8_19", float(100-i))
                time.sleep(.01)


PWM.stop("P8_13")
PWM.cleanup()
