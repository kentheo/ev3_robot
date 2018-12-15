#! /usr/bin/env python
# Core imports
import time
import datetime
import ev3dev.ev3 as ev3

# Local Imports
import testing as testing
import utilities as util
import openLoopControl as olc

# Step D: Use a class to develop a bigger program with a state
#o = olc.openLoopControl()
## execute (with default params)
#o.operateWheels()

btn = ev3.Button()
val = True
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outB')
motor_left.connected
motor_right.connected
kp = 0.15
ki = 0.06
kd = 0.15
offset = 45
tp = 22
integral = 0
lastError = 0
derivative = 0

while(val == True and (not btn.backspace)):
   color = testing.senseColor()
   error = offset - color
   if(color>88):
	  print 'ooooooooooooooooooooooooooo'
          testing.stop()
          val = False
   color = testing.senseColor()
   testing.pid_left_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative)
   
testing.stop()
ev3.Sound.speak('I\'ll be back').wait()


	  #if ( seen_white == True):
               #second_time = util.timestamp_now()
               #print "I HAVE SEEN WHITEEEE TWICE!!!!!!!"
               #print second_time
               #difference = second_time - first_time
               #print difference
               #if(difference >= 0.5E3):
                    #testing.stop()
                    #val= False
                    #ev3.Sound.speak('I reached the end').wait()
          #else:
               #first_time = util.timestamp_now()
               #print "WHITE FOR THE FIRST TIMEE******"
               #seen_white = True
   #else:
        #seen_white = False


   #if (abs(error) <= 15):
               #integral = (1/3)*integral + error
   #else:
       #integral = (2/3)*integral + error

