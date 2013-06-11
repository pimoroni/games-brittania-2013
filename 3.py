#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import uinput

# assign our communication pins and pulse length
dataPin  = 4
clockPin = 10
latchPin = 11
pulseLength = 2 / 1000000

# set the GPIO pin numbering mode
GPIO.setmode(GPIO.BCM)

# setup the GPIO pin modes
GPIO.setup(dataPin,  GPIO.IN)
GPIO.setup(clockPin, GPIO.OUT)
GPIO.setup(latchPin, GPIO.OUT)

# reset the latchPin and clockPin to LOW (0)
GPIO.output(latchPin, GPIO.LOW)
GPIO.output(clockPin, GPIO.LOW)
sleep(pulseLength)

# create a list of the uinput constants for each button
buttons = (uinput.BTN_LEFT, uinput.KEY_SPACE, uinput.KEY_3, uinput.KEY_4, uinput.KEY_W, uinput.KEY_S, uinput.KEY_A, uinput.KEY_D, uinput.BTN_RIGHT, uinput.KEY_6, uinput.KEY_Q, uinput.KEY_E)

# create a uinput device to emit the keypresses with
device = uinput.Device(buttons)

# loop forever
while True:

	# set latchPin HIGH (1) for at least 200ns 
        # to store the current button state in the 
	# shift register
	GPIO.output(latchPin, GPIO.HIGH)
	sleep(pulseLength)
	GPIO.output(latchPin, GPIO.LOW)
	sleep(pulseLength)

	# read the dataPin once for each button to
	# retrieve their state
	for i in range(0, 12):
		# reads the button state and prints it out
		buttonState = GPIO.input(dataPin)

		if buttonState == GPIO.LOW:
			# if the button is pressed then emit it
			if buttons[i] == uinput.KEY_Q:
				device.emit(uinput.REL_X, -30)
			elif buttons[i] == uinput.KEY_E:
				device.emit(uinput.REL_X, 30)
			else:
				device.emit(buttons[i], 1)			
		else:
			device.emit(buttons[i], 0)			
		
		# pulse the clock signal
		GPIO.output(clockPin, GPIO.HIGH)
		sleep(pulseLength)
		GPIO.output(clockPin, GPIO.LOW)
		sleep(pulseLength)
	
	# wait
	# you wait, time passes
	sleep(0.05)
