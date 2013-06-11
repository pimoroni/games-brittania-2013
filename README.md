Interfacing a SNES controller via the Raspberry Pi GPIO
=======================================================

This repository contains the Pimoroni workshop materials for their Games Brittania 2013 workshop "Interfacing a SNES controller via the Raspberry Pi GPIO".

You may want to install required packages by running the following command:

    sudo apt-get install python-pip libudev-dev
    sudo pip install python-uinput

- 1.py: Reads the SNES controller button state from the GPIO and outputs a bitmask
- 2.py: As above but also maps the button state to characters and outputs them on the screen instead of a bitmask
- 3.py: As above but uses uinput to generate fake keypresses instead of outputting on the screen
