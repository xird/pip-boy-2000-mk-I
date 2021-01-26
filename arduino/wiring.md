# Pip-boy 2000 Mk.I wiring

BEFORE YOU START: Read the full instructions and don't forget the resistors!

## Arduino Nano Every pins:

8 - rotary encoder button
4 - push button "archives"
5 - push button "close"
11 - push button "status"
12 - push button "automaps"
7 - rotary encoder data
6 - rotary encoder clock
13 - TX unconnected / RP serial RX
39 - RX unconnected / RP serial TX
A7 - pot 0 middle
A6 - pot 1 middle

Arduino Nano Every ground should be connected to:

- pot 0 left
- pot 1 left
- rotary encoder gnd
- vacuum tube LED grounds

Arduino Nano Every +5V should be connected to:

- vacuum tube LED resistors
- rotary encoder +
- each push button
- pot 0 right
- pot 1 right

## Resistors

- Between each vacuum tube LED positive leg and +5V. Select a suitable size based on your LED and how bright you want it to be.
- Pull-down resistors between each Nano push button pin(4, 5, 8, 11, 12) and ground. 5kohm works well.
- Potentiometer values don't matter. Go with 10kohm, for example.

## Hints:

- Assemble the connections one component at a time, and confirm that they work correctly before moving on to the next one.
- Upload the sketch to the Arduino before starting. This way you can use the Arduino IDE Serial monitor to see what is being sent when the buttons are pushed.
- Don't worry about pins 13 and 39 unless you know you want to go that route.
- This guide has been written from memory, as I didn't want to open the Pip-boy once I got it working. As such, the above may not be 100% accurate.
