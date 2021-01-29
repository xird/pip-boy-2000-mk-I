# pip-boy-2000-mk-I

A Pip-boy prop based on the original Pip-boy 2000 from Fallout 1 &amp; 2

## Summary

- 3D-printed case
- Runs on a Raspberry Pi / Raspbian with an LCD
- Inputs handled by Arduino Nano Every. Sent to the RasPi via serial
- RasPi receives the serial data and turns them into keypresses with a Python script
- The keypresses are handled by a custom HTML / JS page that generates the Pip-boy UI

## Resources

- First build log post in my blog: http://blog.ampli.fi/fallout-1-2-style-pip-boy-2000-replica-part-1-design/
- Thread on the RPF: https://www.therpf.com/forums/threads/pip-boy-2000-mk-i-from-fallout-1-fallout-2.329566/
- STL files on Thingiverse: TODO
- Test run the "Pip-boy UI site" here: http://ampli.fi/pip-boy

## Included in this repository

### html

The website that looks like a Pip-boy UI.

### Arduino

- The sketch running on the Nano Every that takes input from the physical buttons etc. and sends events via the serial port.
- Wiring instructions in `arduino/wiring.md`

### Python

The simple script running on the RasPi that receives the serial events and turns them into keypresses that can be handled by the HTML page.

## Installation

NOTE: These instructions may not be 100% accurate. I've never installed the Pip-boy from scratch, as I've just made changes over time until it works. If you have any corrections, please leave a comment(or better yet, a PR).

### Arduino

Simple enough: Open the sketch in the Arduino IDE, and compile and upload it to the Nano Every.

- You may need to install support for the Every using the Board Manager
- You will need to install support the rotary encoder library "RotaryEncoder" by Matthias Hertel

To deal with the wiring it's probably easiest to create a shield from a piece of perfboard, and solder all the wires on that. For the wiring "diagram" see `arduino/wiring.md`

Once the sketch is loaded on the Every, connect it to the Pi with a micro-USB cable. Note that you will probably need to hack the ends of the cable to make it fit inside the Pip-boy case.

### Raspberry Pi

- I used Raspberry Pi 3, as it was easier to deal with the HDMI connector (micro HDMI on the RP4) to the display, as well as the USB power leads(USB-C on the RP4)

- Install Raspbian
- Clone this Git repository to the Desktop
- Turn the display sideways by adding the following line to `/boot/config.txt` under `[all`]:
`display_rotate=1`

To start Chromium fullscreen with the Pip-boy UI page:
- Edit `/etc/xdg/lxsession/LXDE-pi/autostart`, and add the following line:
`@chromium-browser --kiosk --start-fullscreen --noerrdialogs --disable-session-crashed-bubble --disable-infobars --check-for-update-interval=604800 --disable-pinch /home/pi/Desktop/pip-boy-2000-mk-I/html/index.html`

To hide the mouse cursor:
`sudo apt-get install unclutter`

### Python on the Pi

- `cd python`
- `sudo pip3 install keyboard`
- `sudo pip3 install pyserial`

After that, you can try to run the script with `python pip-boy.py`. Any communication to the serial port should be shown in the terminal.

To make the script run when the Pi is started, add the following line to `/home/pi/.profile`:
`sudo python3 /home/pi/Desktop/pip-boy-2000-mk-I/python/pip-boy.py &`

In case you need more logs saved (note that the previous logs get overwritten as soon as you open a new terminal), change the line to 
`sudo python3 /home/pi/Desktop/pip-boy-2000-mk-I/python/pip-boy.py > /home/pi/pip-boy-out-$(date +"%Y-%m-%dT%H:%M:%S").log 2> pip-boy-error-$(date +"%Y-%m-%dT%H:%M:%S").log &`

Once you've done all the config on the Pi, including the Python config, reboot:
`sudo reboot now`

## Power

My build uses a USB power pack with two USB B outputs. Regular USB Micro B cables connect the power pack to the display and the Pi. One of the cables needs to be spliced with the power leads to the Arduino.
