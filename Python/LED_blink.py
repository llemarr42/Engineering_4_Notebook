# LED Blink (ENGR4)
# written by Loren Lemarr
# 11/22/2021

import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
while True:
	GPIO.output(16, 1)
	print("Blue is off Red is on")
	sleep(.25)
	GPIO.output(16,0)
	GPIO.output(21, 1)
	print("Blue is on Red is off")
	sleep(.25)
	GPIO.output(21, 0)

