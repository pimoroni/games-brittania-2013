Interfacing a SNES controller via the Raspberry Pi GPIO
=======================================================

Note: This repository is out of date and may not work how you expect! If you're interested in using USB devices to control your Python code, you should read: https://learn.pimoroni.com/tutorial/robots/controlling-your-robot-wireless-keyboard

This repository contains the Pimoroni workshop materials for their Games Brittania 2013 workshop "Interfacing a SNES controller via the Raspberry Pi GPIO".

You may want to install required packages by running the following command:

    sudo apt-get install python-pip libudev-dev
    sudo pip install python-uinput

- 1.py: Reads the SNES controller button state from the GPIO and outputs a bitmask
- 2.py: As above but also maps the button state to characters and outputs them on the screen instead of a bitmask
- 3.py: As above but uses uinput to generate fake keypresses instead of outputting on the screen
