#! /usr/bin/env python
# Core imports
import time
import datetime
import ev3dev.ev3 as ev3

import tutorial as tutorial
import utilities as util
import openLoopControl as olc

gyro_sensor = ev3.GyroSensor(ev3.INPUT_1)
gyro_sensor.mode = 'GYRO-G&A'
gyro_sensor.mode = 'GYRO-ANG'
gyro_sensor.connected

#t_start = util.timestamp_now()
#degrees = gyro_sensor.value()
#print degrees
#while True:
 #       tutorial.moveForward()
  #      degrees = gyro_sensor.value()
   #     print degrees
    #    t_now = util.timestamp_now()
     #   if (t_now - t_start > 2E3):
      #      print ("finishing")
       #     break
tutorial.rotateRobot(100,50,90)
