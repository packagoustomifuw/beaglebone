#!/usr/bin/python

from Adafruit_I2C import Adafruit_I2C as I2C
import time
import os

#IMU class for Sparkfun LSM9DS1 9-axis IMU
class IMU(object)

   #constructor
   def __init__(self, device_add, accel_gyro_add, mag_add)
      #Assign the given device address, accelerometer and gyroscope register address, and magnetometer address
      self.device_add = I2C(device_add)
      self.accel_gyro_add = I2C(accel_gyro_add)
      self.mag_add = I2C(mag_add)

#set I2C address for accelerometer and gyroscope
accgy = I2C(0x6b)
#set I2C address for magnetometer
mag = I2C(0x1e)

#set angles and axes
pitch_high = 0x19
pitch_low = 0x18
roll_high = 0x1b
roll_low = 0x1a
yaw_high = 0x1d
yaw_low = 0x1c
x_axis_high = 0x29
x_axis_low = 0x28
y_axis_high = 0x2b
y_axis_low = 0x2a
z_axis_high = 0x2d
z_axis_low = 0x2c

#initialize IMU

#set accelerometer and gyroscope data rate
I2C.write8(accgy, 0x10, 0xc0) #0xc0 is 952 Hz
I2C.write8(accgy, 0x20, 0xc0) 

#set high resolution mode for accelerometer
#I2C.write8(accgy, 0x21, 0x80)

#set continuous FIFO mode
I2C.write8(accgy, 0x2E, 0xc0)

while True:

   #print (I2C.readS

   #read pitch data
   print "Pitch rate = "
   print ((I2C.readS8(accgy, pitch_high) << 8) | I2C.readS8(accgy, pitch_low)) / 133.747
   
   #read roll data
   print "Roll rate = "
   print ((I2C.readS8(accgy, roll_high) << 8) | I2C.readS8(accgy, roll_low)) / 133.747

   #read yaw data
   print "Yaw rate = "
   print ((I2C.readS8(accgy, yaw_high) << 8) | I2C.readS8(accgy, yaw_low)) / 133.747

   #read x data
   print "x linear rate = "
   print -1 * ((I2C.readS8(accgy, x_axis_high) << 8) | I2C.readS8(accgy, x_axis_low)) / 16536.0

   #read y data
   print "y linear rate = "
   print -1 * ((I2C.readS8(accgy, y_axis_high) << 8) | I2C.readS8(accgy, y_axis_low)) / 16536.0

   #read z data
   print "z linear rate = "
   #trying this out. data * 3.3 V / 65536 (16 bits)
   print -1 * ((I2C.readS8(accgy, z_axis_high) << 8) | I2C.readS8(accgy, z_axis_low)) / 16536.0

   #delay for 100 ms
   time.sleep(.1)
   
   #clear screen
   os.system('clear')
