#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C as I2C
import time
import os
import math

#set I2C address for sensor
addr = I2C(0x40)

#set temp, humidity, and initialization register addresses
temp = 0x00
humi = 0x01
init = 0x02

#initialize sensor to come out of sleep
I2C.write16(addr, init, 0x1000) #setting bit 12 to 1 to get temp and humidity readings in 14 bit resolution
I2C.write16(addr, temp, 0x0000) #start a pointer write transaction to temp register
time.sleep(0.5) #delay to allow data conversion 

while True:

   #read temp data
   print "Temp data = "
   print I2C.readU16(addr, temp) / math.pow(2,16) * 165 - 40
   print " C"
   time.sleep(0.01)   

   #read roll data
   print "Humidity data = "
   print I2C.readU16(addr, humi) / math.pow(2,16) * 100
   print "%"
   time.sleep(0.01)

   #clear screen
   os.system('clear')
