#! /usr/bin/env python
# Core imports
import ev3dev.ev3 as ev3
# Local Imports
import functions as functions
#Initialise variables
kp = 0.20
ki = 0.05
kd = 0.20
offset = 45
tp = 22
integral = 0
lastError = 0
derivative = 0
btn = ev3.Button()

ev3.Sound.speak('Task A').wait()
while(not btn.backspace):
   color = functions.senseColor() 
   if(color>86):
          functions.stop()
          break
   #Use PID to move the robot along the line
   error = offset - color
   functions.pid_left_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative)
   

functions.stop()
ev3.Sound.speak('End of the line').wait()
ev3.Sound.speak('End of task A').wait()

