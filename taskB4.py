#! /usr/bin/env python
# Core imports
import ev3dev.ev3 as ev3

# Local Imports
import functions as functions

#Initialise variables
kp = 0.15
ki = 0.06
kd = 0.15
offset = 45
tp = 22
error = 0
lastError = 0
integral = 0
derivative = 0
count = 0
btn = ev3.Button()

#Initialise gyro sensor
gyro_sensor = ev3.GyroSensor(ev3.INPUT_1)
gyro_sensor.mode = 'GYRO-G&A'
gyro_sensor.mode = 'GYRO-ANG'
degrees = gyro_sensor.value()

ev3.Sound.speak('Task B').wait()
while(not btn.backspace):
   ev3.Sound.speak('Following left line').wait()
   color = functions.senseColor()
   # Inner left and must turn right to find line
   moved = False
   degrees1 = gyro_sensor.value()
   while(moved == False):         
         functions.pid_left_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative)
         color = functions.senseColor()
         #When white found, stop
         if (color >= 80):
            functions.stop()
            moved = True
   if(color>=80):
          functions.stop()
          degrees2 = gyro_sensor.value()
          if (not(degrees1 == degrees2)):
              ev3.Sound.speak('Adjusting my position').wait()
              while(degrees2 < degrees1):
                   functions.inverseRight()
                   degrees2 = gyro_sensor.value()
          functions.stop()
          ev3.Sound.speak('End of line').wait()
          ev3.Sound.speak('I will look for a line on my right').wait()
          degrees = gyro_sensor.value()
          #Turn right using gyro sensor
          while(abs(gyro_sensor.value()-degrees) < 85):
              functions.inverseRight()
          functions.stop()
          color = functions.senseColor()
          #Turned right and will move forward to find another line
          while(color>=70):
              functions.moveForward()
              color = functions.senseColor()          
          functions.stop()
          ev3.Sound.speak('Found the line')
          #Turn left using gyro sensor
          degrees = gyro_sensor.value()
          while(abs(gyro_sensor.value()-degrees) < 81):
              functions.turnLeft()
          functions.stop()          
          #Initialise function values
          error = 0
          lastError = 0
          integral = 0
          derivative = 0
          ev3.Sound.speak('Following right line').wait()
          # Move to the right internal
          color = functions.senseColor()
          moved = False
          degrees1 = gyro_sensor.value()
          while (moved == False):
                functions.pid_right_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative)
                color = functions.senseColor()
                if (color >= 85):
                   functions.stop()
                   moved = True
          #Robot must go through two right lines exactly
          count = count + 1
          if (count > 1):
              break 
          degrees2 = gyro_sensor.value()
          if (not(degrees1 == degrees2)):
              ev3.Sound.speak('Adjusting my position').wait()
              while(degrees2 > degrees1):
                   functions.inverseLeft()
                   degrees2 = gyro_sensor.value()
          functions.stop() 
          ev3.Sound.speak('End of the line').wait()
          ev3.Sound.speak('I will look for a line on my left').wait()
          degrees = gyro_sensor.value()
          #Turn left using gyro sensor
          while(abs(gyro_sensor.value()-degrees) < 90):
              functions.inverseLeft()
          functions.stop()
          color = functions.senseColor()
          while(color>=70):
              functions.moveForward()
              color = functions.senseColor()
          functions.stop()
          #Turn right using gyro sensor
          degrees = gyro_sensor.value()
          while(abs(gyro_sensor.value()-degrees) < 88):
              functions.turnRight()
          functions.stop()          
          ev3.Sound.speak('Found the line')
          error = 0
          lastError = 0
          integral = 0
          derivative = 0        
functions.stop()
ev3.Sound.speak('End of task B').wait()
