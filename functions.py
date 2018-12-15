import ev3dev.ev3 as ev3
import time

# Output
motor_left = ev3.LargeMotor('outA')
motor_right = ev3.LargeMotor('outB')
motor_servo = ev3.MediumMotor('outC')

# Input - Sensors
color_sensor = ev3.ColorSensor(ev3.INPUT_3)
ultrasonic_sensor = ev3.UltrasonicSensor(ev3.INPUT_2)
#gyro_sensor = ev3.GyroSensor(ev3.INPUT_4)

def stop():
    motor_left.stop_action='brake'
    motor_right.stop_action='brake'
    motor_left.stop()
    motor_right.stop()
    time.sleep(2)

def moveForward():
    motor_left.connected
    motor_right.connected
    motor_left.run_direct(duty_cycle_sp=32)
    motor_right.run_direct(duty_cycle_sp=32)

def turnLeft():
    motor_left.connected
    motor_right.connected
    motor_left.run_direct(duty_cycle_sp=5)
    motor_right.run_direct(duty_cycle_sp=35)

def turnRight():
    motor_left.connected
    motor_right.connected
    motor_left.run_direct(duty_cycle_sp=35)
    motor_right.run_direct(duty_cycle_sp=-10)

def senseColor():
    color_sensor.connected
    color_sensor.mode = 'COL-REFLECT'
    return color_sensor.value()

def distance():
    ultrasonic_sensor.connected
    ultrasonic_sensor.mode = 'US-DIST-CM'
    return ultrasonic_sensor.value()

def recordUltraSonic():
    print("Record readings from ultrasonic")
    print("Will print after back button is pressed")

    btn = ev3.Button()

    ultrasonic_sensor.connected
    ultrasonic_sensor.mode = 'US-DIST-CM' # will return value in mm

    readings = ""
    readings_file = open('results.txt', 'w')

    while not btn.backspace:
        readings = readings + str(ultrasonic_sensor.value()) + '\n'
    readings_file.write(readings)
    readings_file.close() # Will write to a text file in a column
    print 'i just printed your results>>>>>>>>>>>>>>>>>>>>'

def pid_left_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative):
    motor_left.connected
    motor_right.connected
    error = offset - color
    integral = integral + error
    derivative = error - lastError
    turn = kp * error + ki * integral + kd * derivative
    powerA = tp + turn
    powerB = tp - turn 
    motor_left.run_direct(duty_cycle_sp=powerA)
    motor_right.run_direct(duty_cycle_sp=powerB)
    lastError = error

def pid_right_internal(offset, error, lastError, color, kp, ki, kd, tp, integral, derivative):
    motor_left.connected
    motor_right.connected
    error = color - offset
    integral = integral + error
    derivative = error - lastError
    turn = kp * error + ki * integral + kd * derivative
    powerA = tp + turn
    powerB = tp - turn 
    motor_left.run_direct(duty_cycle_sp=powerA)
    motor_right.run_direct(duty_cycle_sp=powerB)
    lastError = error

def servoSensor():
    ultrasonic_sensor.connected
    motor_servo.connected
    speed=-35
    motor_servo.run_timed(time_sp=420, duty_cycle_sp=speed)
    time.sleep(0.6)  


def servoSensor_return():
    ultrasonic_sensor.connected
    motor_servo.connected
    speed=35
    motor_servo.run_timed(time_sp=400, duty_cycle_sp=speed)
    time.sleep(0.5)   

def pid_obstacle(offset, error, lastError, distance, kp, ki, kd, tp, integral, derivative):
    motor_left.connected
    motor_right.connected
    error = offset - distance
    integral = integral + error
    derivative = error - lastError
    turn = kp * error + ki * integral + kd * derivative
    if (distance > 200):
        powerA = tp + 4     
        powerB = tp + 22
    else:
        powerA = tp + turn
        powerB = tp - turn
    motor_left.run_direct(duty_cycle_sp=powerA)
    motor_right.run_direct(duty_cycle_sp=powerB)
    lastError = error

def inverseRight():
    motor_left.connected
    motor_right.connected
    motor_left.run_direct(duty_cycle_sp=35)
    motor_right.run_direct(duty_cycle_sp=-35)

def inverseLeft():
    motor_left.connected
    motor_right.connected
    motor_left.run_direct(duty_cycle_sp=-35)
    motor_right.run_direct(duty_cycle_sp=35)

def pid_test_p(offset, error, color, kp, tp):
    motor_left.connected
    motor_right.connected
    error = offset - color
    turn = kp * error
    powerA = tp + turn
    powerB = tp - turn 
    motor_left.run_direct(duty_cycle_sp=powerA)
    motor_right.run_direct(duty_cycle_sp=powerB)

def pid_test_pi(offset, error, color, kp, ki, tp, integral):
    motor_left.connected
    motor_right.connected
    error = offset - color
    integral = integral + error
    turn = kp * error + ki * integral
    powerA = tp + turn
    powerB = tp - turn 
    motor_left.run_direct(duty_cycle_sp=powerA)
    motor_right.run_direct(duty_cycle_sp=powerB)


