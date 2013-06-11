#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import subprocess

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

buttons = ('B', 'Y', 'SELECT', 'START', 'UP', 'DOWN', 'LEFT', 'RIGHT', 'A', 'X', 'S-LEFT', 'S-RIGHT')

# loop forever
while True:

	# set latchPin HIGH (1) for at least 200ns 
        # to store the current button state in the 
	# shift register
	GPIO.output(latchPin, GPIO.HIGH)
	sleep(pulseLength)
	GPIO.output(latchPin, GPIO.LOW)
	sleep(pulseLength)

	# create a blank message to output	
	message = ''

	# read the dataPin once for each button to
	# retrieve their state
	for i in range(0, 12):
		# reads the button state and prints it out
		buttonState = GPIO.input(dataPin)

		if buttonState == GPIO.LOW:
			# if the button is pressed then retrieve
			# name and add it to the message
			message = message + buttons[i] + ' '			
		
		# pulse the clock signal
		GPIO.output(clockPin, GPIO.HIGH)
		sleep(pulseLength)
		GPIO.output(clockPin, GPIO.LOW)
		sleep(pulseLength)
	
	# clear the screen
	subprocess.call('clear')
	
	# output the message in mahoosive text!
	if message != '':
		subprocess.call(['figlet', '-c', '-k', '-f', 'banner', message])

	# wait
	# you wait, time passes
	sleep(0.5)
