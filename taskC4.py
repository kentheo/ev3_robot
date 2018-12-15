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

kp2 = 0.3
ki2 = 0.06
kd2 = 0.15
offset2 = 120
tp2 = 25
error2 = 0
lastError2 = 0
integral2 = 0
derivative2 = 0

btn = ev3.Button()
#Initialise gyro sensor
gyro_sensor = ev3.GyroSensor(ev3.INPUT_1)
gyro_sensor.mode = 'GYRO-G&A'
gyro_sensor.mode = 'GYRO-ANG'

while((not btn.backspace)):
   
   color = functions.senseColor()    
   while(color <= 87):         
           functions.pid_left_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative)
           color = functions.senseColor()
           dist = functions.distance()
           if (dist <= 70):
		       functions.stop() 
		       ev3.Sound.speak('There is an obstacle').wait()
		       #turn right using gyro sensor
		       degrees = gyro_sensor.value()
		       #turn right
		       while((gyro_sensor.value()-degrees) < 95):
			    functions.inverseRight()
		       functions.stop()
		       functions.servoSensor()
		       ev3.Sound.speak('I turned right to avoid it').wait()

		       color = functions.senseColor()
		       dist = functions.distance()
		       while (color >=55):
			     # pid
		             functions.pid_obstacle(offset2, error2, lastError2, dist, kp2, ki2, kd2, tp2, integral2, derivative2)
			     dist = functions.distance()
		             color = functions.senseColor()
		       functions.stop()
		       ev3.Sound.speak('I went past the obstacle').wait()
		       degrees = gyro_sensor.value()
		       functions.servoSensor_return()
                       color = functions.senseColor()
                       while (color < 80):
                             functions.moveForward()
                             color = functions.senseColor()
                       functions.stop()
                       color = functions.senseColor()
                       while(color>65):
                            functions.turnRight()
                            color = functions.senseColor()
	       ##continue with PID
functions.stop()
ev3.Sound.speak('End of task C').wait()
