#! /usr/bin/env python
# Core imports
import ev3dev.ev3 as ev3

# Local Imports
import functions as functions

print("Record readings from color sensor")
print("Will print after back button is pressed")

btn = ev3.Button()

sonar = ev3.ColorSensor(ev3.INPUT_3)
sonar.connected
sonar.mode = 'COL-REFLECT'

readings = ""
readings_file = open('results___.txt', 'w')

while not btn.backspace:
	readings = readings + str(sonar.value()) + '\n'
readings_file.write(readings)
readings_file.close() # Will write to a text file in a column
