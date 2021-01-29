import keyboard
import serial
import time
import subprocess
import re
from pathlib import Path
import time

# Check that the script isn't already running
processes = subprocess.check_output(["/bin/ps", "-aux"]).decode(encoding='ascii')
print(processes)
pythons = re.finditer('python', processes)
pythoncount = 0
for python in pythons:
  pythoncount = pythoncount + 1

# The expected value is 2; This script with and without "sudo"
if pythoncount > 2:
  print('Looks like this script is already running')
  exit(1)

# Check that the serial port is available
portfilepath = '/dev/ttyACM0'
portfile = Path(portfilepath)
while not portfile.exists():
  print('No /dev/ttyAC0 available...')
  time.sleep(2) 

print('Found /dev/ttyAC0')
ser = serial.Serial(portfilepath)
pot = [0, 0];

while True:
  data = ser.readline().strip().decode(encoding='ascii', errors="ignore")
  command = data.split(' ')

  if command[0] == 'rot':
    if command[1] == '1':
      print('UP')
      keyboard.press_and_release("up")
    elif command[1] == '-1':
      print('DOWN')
      keyboard.press_and_release("down")
    else:
      print('Unknown rot command "' + data  + '"');
  elif command[0] == 'pot':
    # This should be filtered on the Arduino, but I can't be bothered opening the Pip-boy just now.
    poti = int(command[1]);
    diff = pot[poti] - int(command[2]);
    # print(diff)
    if abs(diff) > 10:
      print(data);
      keyboard.write(command[1] + command[2] + ' ')
      pot[poti] = int(command[2])
  elif command[0][:1] == 'B':
    if command[0][1:] == '11':
      print('STATUS')
      keyboard.press_and_release("s")
    elif command[0][1:] == '12':
      keyboard.press_and_release("m")
      print('AUTOMAPS')
    elif command[0][1:] == '4':
      keyboard.press_and_release("r")
      print('ARCHIVES')
    elif command[0][1:] == '5':
      keyboard.press_and_release("c")
      print('CLOSE')
    elif command[0][1:] == '8':
      keyboard.press_and_release("enter")
      print('ENTER')
  else:
    print('Unknown command "' + data + '"');
